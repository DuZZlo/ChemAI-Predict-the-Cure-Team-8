# важнейшие предикторов
core_descriptors = [
    'MolLogP', 'TPSA', 'MolWt', 
    'NumHAcceptors', 'NumHDonors', 
    'NumRotatableBonds', 'Kappa1', 'Kappa2',
    'MaxAbsEStateIndex', 'MinEStateIndex',
    'LabuteASA', 'FractionCSP3',
    'fr_amide', 'fr_nitrile', 'fr_halogen'
]


# расширенный список предикторов
extended_descriptors = core_descriptors + [
    'BCUT2D_CHGHI', 'BCUT2D_CHGLO',
    'PEOE_VSA1', 'PEOE_VSA4', 'PEOE_VSA8',  # полярные зоны
    'SlogP_VSA3', 'SlogP_VSA7',              # гидрофобные зоны
    'Chi1', 'Chi1v', 'Chi2n',                # топологическая связность
    'BalabanJ', 'BertzCT',                   # сложность
    'fr_pyridine', 'fr_phenol', 'fr_ether'   # дополнительные фармакофоры
]