import os, re
import py3Dmol
from rdkit import Chem


def safe_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name)


def get_charge_and_multiplicity(mol):
    """分子から電荷とスピン多重度を推定する。

    電荷は各原子の形式電荷（formal charge）の総和として厳密に計算できる。
    一方スピン多重度は、閉殻分子であれば1（一重項）だが、開殻（ラジカル）分子の
    場合は本来、量子化学計算や実験による確認が必要であり、ここでは
    「不対電子数（ラジカル電子数）+ 1」という簡便な近似式で見積もる。
    この近似は多くの有機分子（閉殻）では常に1になり問題ないが、
    複数の不対電子を持つ分子（三重項カルベン等）では正しい多重度と
    一致しない場合があるため、そのまま計算に使う前に必ず化学的な妥当性を
    確認すること。

    Returns:
        (charge, multiplicity): どちらも int
    """
    charge = Chem.GetFormalCharge(mol)
    n_radical_electrons = sum(atom.GetNumRadicalElectrons() for atom in mol.GetAtoms())
    multiplicity = n_radical_electrons + 1
    return charge, multiplicity


def write_xyz_input(mol, confId, filename, comment=""):
    """指定したコンフォーマーの座標を標準的なXYZ形式で書き出す。

    XYZ形式は1行目が原子数、2行目がコメント行（空でもよい）、
    3行目以降が「元素記号 x y z」という素直なフォーマット。
    """
    try:
        atoms = mol.GetAtoms()
        conf = mol.GetConformer(confId)
        with open(filename, "w") as f:
            f.write(f"{mol.GetNumAtoms()}\n")
            f.write(f"{comment}\n")
            for atom in atoms:
                pos = conf.GetAtomPosition(atom.GetIdx())
                f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")
    except Exception as e:
        print(f"[ERROR] write_xyz_input failed: {filename}")
        raise e


def write_gaussian_input(mol, confId, filename, method="B3LYP", basis="6-31G(d)",
                          title="Gaussian job", charge=None, multiplicity=None,
                          nproc=4, mem="8GB", route_extra="Opt"):
    """指定したコンフォーマーの座標からGaussian用の入力ファイル（.gjf）を書き出す。

    charge・multiplicityを省略した場合は`get_charge_and_multiplicity()`で
    分子から自動計算する（get_charge_and_multiplicity()のdocstring参照。
    ラジカル分子では必ず妥当性を確認すること）。
    """
    if charge is None or multiplicity is None:
        auto_charge, auto_multiplicity = get_charge_and_multiplicity(mol)
        charge = auto_charge if charge is None else charge
        multiplicity = auto_multiplicity if multiplicity is None else multiplicity

    try:
        atoms = mol.GetAtoms()
        conf = mol.GetConformer(confId)
        with open(filename, "w") as f:
            f.write(f"%nproc={nproc}\n%mem={mem}\n")
            f.write(f"#p {route_extra} {method}/{basis}\n\n")
            f.write(f"{title}\n\n")
            f.write(f"{charge} {multiplicity}\n")
            for atom in atoms:
                pos = conf.GetAtomPosition(atom.GetIdx())
                f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")
            f.write("\n")
    except Exception as e:
        print(f"[ERROR] write_gaussian_input failed: {filename}")
        raise e


def show_3D_from_xyz(xyz_path: str, width=400, height=400, background='#e1e1e1'):
    with open(xyz_path, 'r') as f:
        xyz = f.read()

    view = py3Dmol.view(width=width, height=height)
    view.addModel(xyz, 'xyz')
    view.setStyle({'stick': {}})
    view.setBackgroundColor(background)
    view.zoomTo()
    return view.show()
