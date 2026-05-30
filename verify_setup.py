"""
verify_setup.py — Verifica se o ambiente está configurado corretamente
antes de executar os notebooks.

Execute com: python verify_setup.py
"""
import sys
import importlib

REQUIRED = [
    ('numpy', 'numpy'),
    ('pandas', 'pandas'),
    ('cv2', 'opencv-python'),
    ('sklearn', 'scikit-learn'),
    ('skimage', 'scikit-image'),
    ('matplotlib', 'matplotlib'),
    ('seaborn', 'seaborn'),
    ('kagglehub', 'kagglehub'),
    ('tqdm', 'tqdm'),
    ('scipy', 'scipy'),
    ('PIL', 'Pillow'),
]

OPTIONAL = [
    ('shap', 'shap'),
]

print('=' * 55)
print('  Verificação do ambiente — Coffee Inspection Pipeline')
print('=' * 55)

all_ok = True
for mod_name, pkg_name in REQUIRED:
    try:
        mod = importlib.import_module(mod_name)
        ver = getattr(mod, '__version__', '?')
        print(f'  ✅ {pkg_name:<25} v{ver}')
    except ImportError:
        print(f'  ❌ {pkg_name:<25} NÃO INSTALADO  →  pip install {pkg_name}')
        all_ok = False

print()
print('Opcionais:')
for mod_name, pkg_name in OPTIONAL:
    try:
        mod = importlib.import_module(mod_name)
        ver = getattr(mod, '__version__', '?')
        print(f'  ✅ {pkg_name:<25} v{ver}')
    except ImportError:
        print(f'  ⚠️  {pkg_name:<25} não instalado (notebook 04 será afetado)')

print()
# Verifica credenciais Kaggle
import os
kaggle_json = os.path.expanduser('~/.kaggle/kaggle.json')
if os.path.exists(kaggle_json):
    print(f'  ✅ Kaggle API key encontrada em {kaggle_json}')
else:
    env_user = os.environ.get('KAGGLE_USERNAME')
    env_key  = os.environ.get('KAGGLE_KEY')
    if env_user and env_key:
        print('  ✅ Credenciais Kaggle encontradas nas variáveis de ambiente.')
    else:
        print('  ⚠️  Credenciais Kaggle não encontradas.')
        print('     Crie ~/.kaggle/kaggle.json ou defina KAGGLE_USERNAME e KAGGLE_KEY.')

print()
if all_ok:
    print('✅ Ambiente pronto! Execute os notebooks na ordem: 01 → 02 → 03 → (04)')
else:
    print('❌ Corrija as dependências acima e execute novamente.')
    sys.exit(1)
