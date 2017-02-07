indir ='/eos/fcc/hh/generation/mg5_amcatnlo/gridpacks/'
outdir='/eos/fcc/hh/generation/mg5_amcatnlo/lhe/'

version='v0_0'
outdir_delphes='/eos/fcc/hh/generation/DelphesEvents/%s/'%version


gridpacklist = {
'pp_tt012j_5f':['ttbar + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 60, qCut = 90', '4.2670e04',''],
'pp_w012j_5f':['w + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','1.4995e06', ''],
'pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45', '5.1839e05', ''],
'pp_jjaa01j_5f':['dijet diphoton + 0,1,2 jets 5 flavor scheme','xqcut = 20, qCut = 30', '55.72','0.236'],
'pp_jjaa_5f':['dijet diphoton','','17.97','1.0'],
'pp_jjja01j_5f':['photon +jets + 0,1,2,3 jets 5 flavor scheme','xqcut = 20, qCut = 25','4.133e+05','0.143'],
'pp_jjja_5f':['photon +jets','','','1.023e05','1.0'],
'pp_tth':['ttbar plus higgs','inclusive','','23.37','1.0'],
'pp_zh':['z plus higgs production','inclusive','','7.42','1.0'],
'pp_hh':['gluon gluon fusion di-higgs','inclusive','', '0.65','1.0'],
}
