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

# Гипотеза 1: ADME-ядро (биодоступность и лекарственноподобие)
hypothesis_1_adme = [
    'qed', 'MolLogP', 'TPSA', 'NumHAcceptors', 'NumHDonors',
    'NumRotatableBonds', 'MolWt', 'FractionCSP3', 'RingCount',
    'NumAromaticRings', 'BCUT2D_LOGPHI', 'BCUT2D_LOGPLOW',
    'PEOE_VSA1', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4',
    'SlogP_VSA1', 'SlogP_VSA2', 'SlogP_VSA3', 'fr_Al_OH',
    'fr_Ar_OH', 'fr_COO', 'fr_amide', 'fr_NH0', 'fr_NH1',
    'fr_NH2', 'NumHeteroatoms', 'LabuteASA', 'ExactMolWt',
    'NumValenceElectrons', 'HeavyAtomMolWt', 'MolMR'
]

# Гипотеза 2: Топологическая сложность (форма и связность графа)
hypothesis_2_topology = [
    'BalabanJ', 'BertzCT', 'Chi0', 'Chi0v', 'Chi1', 'Chi1v',
    'Chi2v', 'Chi3v', 'Chi4v', 'Kappa1', 'Kappa2', 'Kappa3',
    'HallKierAlpha', 'Ipc', 'AvgIpc', 'MaxEStateIndex',
    'MinEStateIndex', 'MaxAbsEStateIndex', 'BCUT2D_MWHI',
    'BCUT2D_MWLOW', 'BCUT2D_CHGHI', 'BCUT2D_CHGLO', 'RingCount',
    'NumAromaticRings', 'NumAliphaticRings', 'NumSaturatedRings',
    'NumAromaticHeterocycles', 'NumAliphaticCarbocycles',
    'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles',
    'FpDensityMorgan2', 'FpDensityMorgan3'
]

# Гипотеза 3: Электронная реактивность (фармакофор и реакционные центры)
hypothesis_3_electronic = [
    'MaxPartialCharge', 'MinPartialCharge', 'MaxAbsPartialCharge',
    'NumValenceElectrons', 'NumRadicalElectrons', 'EState_VSA1',
    'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5',
    'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9',
    'EState_VSA10', 'EState_VSA11', 'VSA_EState1', 'VSA_EState2',
    'VSA_EState3', 'VSA_EState4', 'VSA_EState5', 'VSA_EState6',
    'VSA_EState7', 'VSA_EState8', 'VSA_EState9', 'VSA_EState10',
    'fr_ketone', 'fr_aldehyde', 'fr_nitrile', 'fr_nitro',
    'fr_imidazole', 'fr_pyridine'
]