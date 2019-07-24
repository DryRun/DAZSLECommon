import os

txt_folder = os.path.expandvars("$CMSSW_BASE/src/DAZSLE/DAZSLECommon/data/baconbits")

baconbits_lists = {
	2016:{
		# For large samples, use un-hadded files on lxplus
		"JetHTRun2016B":"{}/2016/lxplus/JetHTRun2016B.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016B_PromptReco_v2_resub.root"]
		"JetHTRun2016C":"{}/2016/lxplus/JetHTRun2016C.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016C_PromptReco_v2.root"]
		"JetHTRun2016D":"{}/2016/lxplus/JetHTRun2016D.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016D_PromptReco_v2.root"]
		"JetHTRun2016E":"{}/2016/lxplus/JetHTRun2016E.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016E_PromptReco_v2.root"]
		"JetHTRun2016F":"{}/2016/lxplus/JetHTRun2016F.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016F_PromptReco_v1.root"]
		"JetHTRun2016G":"{}/2016/lxplus/JetHTRun2016G.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016G_PromptReco_v1.root"]
		"JetHTRun2016H":"{}/2016/lxplus/JetHTRun2016H.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016H_PromptReco_v2.root"]
		"SingleMuRun2016B":"{}/2016/lxplus/SingleMuRun2016B.txt".format(txt_folder), 
		"SingleMuRun2016C":"{}/2016/lxplus/SingleMuRun2016C.txt".format(txt_folder), 
		"SingleMuRun2016D":"{}/2016/lxplus/SingleMuRun2016D.txt".format(txt_folder), 
		"SingleMuRun2016E":"{}/2016/lxplus/SingleMuRun2016E.txt".format(txt_folder), 
		"SingleMuRun2016F":"{}/2016/lxplus/SingleMuRun2016F.txt".format(txt_folder), 
		"SingleMuRun2016G":"{}/2016/lxplus/SingleMuRun2016G.txt".format(txt_folder), 
		"SingleMuRun2016H":"{}/2016/lxplus/SingleMuRun2016H.txt".format(txt_folder), 
		"JetHTRun2016B_ps10":"{}/2016/lxplus/JetHTRun2016B.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016B_PromptReco_v2_resub.root"]
		"JetHTRun2016C_ps10":"{}/2016/lxplus/JetHTRun2016C.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016C_PromptReco_v2.root"]
		"JetHTRun2016D_ps10":"{}/2016/lxplus/JetHTRun2016D.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016D_PromptReco_v2.root"]
		"JetHTRun2016E_ps10":"{}/2016/lxplus/JetHTRun2016E.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016E_PromptReco_v2.root"]
		"JetHTRun2016F_ps10":"{}/2016/lxplus/JetHTRun2016F.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016F_PromptReco_v1.root"]
		"JetHTRun2016G_ps10":"{}/2016/lxplus/JetHTRun2016G.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016G_PromptReco_v1.root"]
		"JetHTRun2016H_ps10":"{}/2016/lxplus/JetHTRun2016H.txt".format(txt_folder), #["root://cmsxrootd-site.fnal.gov//store/user/jduarte1/zprimebits-v11.062/JetHTRun2016H_PromptReco_v2.root"]
		"SingleMuRun2016B_ps10":"{}/2016/lxplus/SingleMuRun2016B.txt".format(txt_folder), 
		"SingleMuRun2016C_ps10":"{}/2016/lxplus/SingleMuRun2016C.txt".format(txt_folder), 
		"SingleMuRun2016D_ps10":"{}/2016/lxplus/SingleMuRun2016D.txt".format(txt_folder), 
		"SingleMuRun2016E_ps10":"{}/2016/lxplus/SingleMuRun2016E.txt".format(txt_folder), 
		"SingleMuRun2016F_ps10":"{}/2016/lxplus/SingleMuRun2016F.txt".format(txt_folder), 
		"SingleMuRun2016G_ps10":"{}/2016/lxplus/SingleMuRun2016G.txt".format(txt_folder), 
		"SingleMuRun2016H_ps10":"{}/2016/lxplus/SingleMuRun2016H.txt".format(txt_folder), 
		"QCD_HT100to200":"{}/2016/lxplus/QCD_HT100to200_13TeV.txt".format(txt_folder),
		"QCD_HT200to300":"{}/2016/lxplus/QCD_HT200to300_13TeV.txt".format(txt_folder),
		"QCD_HT300to500":"{}/2016/lxplus/QCD_HT300to500_13TeV.txt".format(txt_folder),
		"QCD_HT500to700":"{}/2016/lxplus/QCD_HT500to700_13TeV.txt".format(txt_folder),
		"QCD_HT700to1000":"{}/2016/lxplus/QCD_HT700to1000_13TeV.txt".format(txt_folder),
		"QCD_HT1000to1500":"{}/2016/lxplus/QCD_HT1000to1500_13TeV.txt".format(txt_folder),
		"QCD_HT1500to2000":"{}/2016/lxplus/QCD_HT1500to2000_13TeV.txt".format(txt_folder),
		"QCD_HT2000toInf":"{}/2016/lxplus/QCD_HT2000toInf_13TeV.txt".format(txt_folder),

		# Smaller samples can stay on cmslpc
		"GluGluHToBB_M125_13TeV_powheg_pythia8_CKKW":"{}/2016/cmslpc/GluGluHToBB_M125_13TeV_powheg_pythia8_CKKW.txt".format(txt_folder),
		"VBFHToBB_M_125_13TeV_powheg_pythia8":"{}/2016/cmslpc/VBFHToBB_M_125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.txtt".format(txt_folder),
		"ttHTobb_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/ttHTobb_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8":"{}/2016/cmslpc/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"WWTo4Q_13TeV_powheg":"{}/2016/cmslpc/WWTo4Q_13TeV_powheg.txt".format(txt_folder),
		"ZZ_13TeV_pythia8":"{}/2016/cmslpc/ZZ_13TeV_pythia8.txt".format(txt_folder),
		"WZ_13TeV_pythia8":"{}/2016/cmslpc/WZ_13TeV_pythia8.txt".format(txt_folder),
		"DYJetsToQQ_HT180_13TeV":"{}/2016/cmslpc/DYJetsToQQ_HT180_13TeV.txt".format(txt_folder),
		"DYJetsToLL_M_50_13TeV":"{}/2016/cmslpc/DYJetsToLL_M_50_13TeV.txt".format(txt_folder),
		"ST_t_channel_antitop_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV_powhegV2_madspin":"{}/2016/cmslpc/ST_t_channel_antitop_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV_powhegV2_madspin.txt".format(txt_folder),
		"ST_t_channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV_powhegV2_madspin":"{}/2016/cmslpc/ST_t_channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV_powhegV2_madspin.txt".format(txt_folder),
		"ST_tW_antitop_5f_inclusiveDecays_13TeV_powheg_pythia8_TuneCUETP8M2T4":"{}/2016/cmslpc/ST_tW_antitop_5f_inclusiveDecays_13TeV_powheg_pythia8_TuneCUETP8M2T4.txt".format(txt_folder),
		"ST_tW_top_5f_inclusiveDecays_13TeV_powheg_pythia8_TuneCUETP8M2T4":"{}/2016/cmslpc/ST_tW_top_5f_inclusiveDecays_13TeV_powheg_pythia8_TuneCUETP8M2T4.txt".format(txt_folder),
		"WJetsToQQ_HT_600ToInf_13TeV":"{}/2016/cmslpc/WJetsToQQ_HT_600ToInf_13TeV.txt".format(txt_folder),
		"WJetsToQQ_HT180_13TeV":"{}/2016/cmslpc/WJetsToQQ_HT180_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_70To100_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_70To100_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_600To800_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_600To800_13TeV.txtt".format(txt_folder),
		"WJetsToLNu_HT_100To200_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_100To200_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_200To400_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_200To400_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_400To600_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_400To600_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_600To800_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_600To800_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_800To1200_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_800To1200_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_1200To2500_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_1200To2500_13TeV.txt".format(txt_folder),
		"WJetsToLNu_HT_2500ToInf_13TeV":"{}/2016/cmslpc/WJetsToLNu_HT_2500ToInf_13TeV.txt".format(txt_folder),
		"TT_powheg":"{}/2016/cmslpc/TT_powheg.txt".format(txt_folder),

	},
	2017:{
		"DYJetsToLL_M_50_HT_1200to2500":"{}/2017/DYJetsToLL_M_50_HT_1200to2500_TuneCP5_13TeV.txt".format(txt_folder),
		"DYJetsToLL_M_50_HT_2500toInf":"{}/2017/DYJetsToLL_M_50_HT_2500toInf_TuneCP5_13TeV.txt".format(txt_folder),
		"DYJetsToLL_M_50_HT_400to600":"{}/2017/DYJetsToLL_M_50_HT_400to600_TuneCP5_13TeV.txt".format(txt_folder),
		"DYJetsToLL_M_50_HT_600to800":"{}/2017/DYJetsToLL_M_50_HT_600to800_TuneCP5_13TeV.txt".format(txt_folder),
		"DYJetsToLL_M_50_HT_800to1200":"{}/2017/DYJetsToLL_M_50_HT_800to1200_TuneCP5_13TeV.txt".format(txt_folder),
		"GluGluHToBB_M125":"{}/2017/GluGluHToBB_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"JetHT_Run2017B":"{}/2017/JetHT_Run2017B.txt".format(txt_folder),
		"JetHT_Run2017C":"{}/2017/JetHT_Run2017C.txt".format(txt_folder),
		"JetHT_Run2017D":"{}/2017/JetHT_Run2017D.txt".format(txt_folder),
		"JetHT_Run2017E":"{}/2017/JetHT_Run2017E.txt".format(txt_folder),
		"QCD_HT1000to1500":"{}/2017/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT1500to2000":"{}/2017/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT2000toInf":"{}/2017/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT500to700":"{}/2017/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT700to1000":"{}/2017/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"ST_t-channel_antitop_4f_inclusiveDecays":"{}/2017/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.txt".format(txt_folder),
		"ST_t-channel_top_4f_inclusiveDecays":"{}/2017/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.txt".format(txt_folder),
		"ST_tW_antitop_5f_inclusiveDecays":"{}/2017/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.txt".format(txt_folder),
		"ST_tW_top_5f_inclusiveDecays":"{}/2017/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.txt".format(txt_folder),
		"TTTo2L2Nu":"{}/2017/TTTo2L2Nu_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
		"TTToHadronic":"{}/2017/TTToHadronic_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
		"TTToSemiLeptonic":"{}/2017/TTToSemiLeptonic_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
		"VBFHToBB_M_125":"{}/2017/VBFHToBB_M_125_13TeV_powheg_pythia8_weightfix.txt".format(txt_folder),
		"WJetsToLNu_HT-1200To2500":"{}/2017/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-200To400":"{}/2017/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-2500ToInf":"{}/2017/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-400To600":"{}/2017/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-600To800":"{}/2017/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-800To1200":"{}/2017/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToQQ_HT-800toInf_qc19_3j":"{}/2017/WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV.txt".format(txt_folder),
		"WJetsToQQ_HT400to600_qc19_3j":"{}/2017/WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV.txt".format(txt_folder),
		"WJetsToQQ_HT600to800_qc19_3j":"{}/2017/WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV.txt".format(txt_folder),
		"WW":"{}/2017/WW_TuneCP5_13TeV-pythia8.txt".format(txt_folder),
		"WZ":"{}/2017/WZ_TuneCP5_13TeV-pythia8.txt".format(txt_folder),
		"WminusH_HToBB_WToQQ_M125":"{}/2017/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"WplusH_HToBB_WToQQ_M125":"{}/2017/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZH_HToBB_ZToNuNu_M125":"{}/2017/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZH_HToBB_ZToQQ_M125":"{}/2017/ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZJetsToQQ_HT-800toInf_qc19_4j":"{}/2017/ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV.txt".format(txt_folder),
		"ZJetsToQQ_HT400to600_qc19_4j":"{}/2017/ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV.txt".format(txt_folder),
		"ZJetsToQQ_HT600to800_qc19_4j":"{}/2017/ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV.txt".format(txt_folder),
		"ZZ":"{}/2017/ZZ_TuneCP5_13TeV-pythia8.txt".format(txt_folder),
		"ggZH_HToBB_ZToQQ_M125":"{}/2017/ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ttHTobb_M125":"{}/2017/ttHTobb_M125_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
	},
	2018:{
		"DYJetsToLL_M-50":"{}/2018/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"GluGluHToBB_M125_amcatnloFXFX_pythia8":"{}/2018/GluGluHToBB_M125_13TeV_amcatnloFXFX_pythia8.txt".format(txt_folder),
		"GluGluHToBB_M125_powheg_pythia8":"{}/2018/GluGluHToBB_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"GluGluHToBB_M125_LHEHpT_250_Inf_amcatnloFXFX_pythia8":"{}/2018/GluGluHToBB_M125_LHEHpT_250_Inf_13TeV_amcatnloFXFX_pythia8.txt".format(txt_folder),
		"JetHT_Run2018A":"{}/2018/JetHT_Run2018A.txt".format(txt_folder),
		"JetHT_Run2018B":"{}/2018/JetHT_Run2018B.txt".format(txt_folder),
		"JetHT_Run2018C":"{}/2018/JetHT_Run2018C.txt".format(txt_folder),
		"JetHT_Run2018D":"{}/2018/JetHT_Run2018D.txt".format(txt_folder),
		"QCD_HT1000to1500":"{}/2018/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT1500to2000":"{}/2018/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT2000toInf":"{}/2018/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT500to700":"{}/2018/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"QCD_HT700to1000":"{}/2018/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"ST_t-channel_antitop_4f_inclusiveDecays":"{}/2018/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.txt".format(txt_folder),
		"ST_t-channel_top_4f_inclusiveDecays":"{}/2018/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.txt".format(txt_folder),
		"ST_tW_antitop_5f_inclusiveDecays":"{}/2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.txt".format(txt_folder),
		"ST_tW_top_5f_inclusiveDecays":"{}/2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.txt".format(txt_folder),
		"SingleMuon_Run2018A":"{}/2018/SingleMuon_Run2018A.txt".format(txt_folder),
		"SingleMuon_Run2018B":"{}/2018/SingleMuon_Run2018B.txt".format(txt_folder),
		"SingleMuon_Run2018C":"{}/2018/SingleMuon_Run2018C.txt".format(txt_folder),
		"SingleMuon_Run2018D":"{}/2018/SingleMuon_Run2018D.txt".format(txt_folder),
		"TTTo2L2Nu":"{}/2018/TTTo2L2Nu_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
		"TTToHadronic":"{}/2018/TTToHadronic_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
		"TTToSemiLeptonic":"{}/2018/TTToSemiLeptonic_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),
		"VBFHToBB_M_125":"{}/2018/VBFHToBB_M_125_13TeV_powheg_pythia8_weightfix.txt".format(txt_folder),
		"WJetsToQQ_HT-800toInf_qc19_3j":"{}/2018/WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV.txt".format(txt_folder),
		"WJetsToQQ_HT400to600_qc19_3j":"{}/2018/WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV.txt".format(txt_folder),
		"WJetsToQQ_HT600to800_qc19_3j":"{}/2018/WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV.txt".format(txt_folder),
		"WminusH_HToBB_WToQQ_M125":"{}/2018/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"WplusH_HToBB_WToQQ_M125":"{}/2018/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZH_HToBB_ZToNuNu_M125":"{}/2018/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZH_HToBB_ZToQQ_M125":"{}/2018/ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ZJetsToQQ_HT-800toInf_qc19_4j":"{}/2018/ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV.txt".format(txt_folder),
		"ZJetsToQQ_HT400to600_qc19_4j":"{}/2018/ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV.txt".format(txt_folder),
		"ZJetsToQQ_HT600to800_qc19_4j":"{}/2018/ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV.txt".format(txt_folder),
		"ggZH_HToBB_ZToQQ_M125":"{}/2018/ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8.txt".format(txt_folder),
		"ttHTobb_M125":"{}/2018/ttHTobb_M125_TuneCP5_13TeV_powheg_pythia8.txt".format(txt_folder),

		# Diboson and wlnu: 2017 for now
		"WW":"{}/2017/WW_TuneCP5_13TeV-pythia8.txt".format(txt_folder),
		"WZ":"{}/2017/WZ_TuneCP5_13TeV-pythia8.txt".format(txt_folder),
		"ZZ":"{}/2017/ZZ_TuneCP5_13TeV-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-1200To2500":"{}/2017/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-200To400":"{}/2017/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-2500ToInf":"{}/2017/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-400To600":"{}/2017/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-600To800":"{}/2017/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
		"WJetsToLNu_HT-800To1200":"{}/2017/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.txt".format(txt_folder),
	},
}

baconbits = {}
for year, sampledict in baconbits_lists.iteritems():
	baconbits[year] = {}
	for sample, txt_path in sampledict.iteritems():
		baconbits[year][sample] = [line.strip() for line in open(txt_path, 'r')]