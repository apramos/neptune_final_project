#! /usr/bin/env python
import re 

AcessDict={	
'X56788':'494_Loligo_forbesi',
'AY450853':'493_Loligo_pealii',
'Z49108':'499_Loligo_subulata',
'AF000947':'492_Sepia_officinalis',
'X70498':'480_Todarodes_pacificus',
'X07797':'475_Enteroctopus_dofleini',
'L03781':'520_Limulus_polyphemus',
'L03782':'530_L_polyphemus',
'DQ852576':'487_Euphausia_superba',
'DQ852587':'515_Homarus_gammarus',
'AF003544':'526_Cambarellus_shufeldtii',
'AF003543':'529_Cambarus_ludovicianus',
'AF003545':'530_Orconectes_virilis',
'AF003546':'522_Procambarus_milleri',
'S53494':'533_Procambarus_clarkii',
'DQ852573':'496_Archaeomysis_grebnitzkii',
'DQ852581':'512_Holmesimysis_costata',
'DQ852591':'501_Mysis_diluviana',
'DQ852592':'520_Neomysis_americana',
'DQ646869':'489_Neogonodactylus_oerstediiRh1',
'DQ646870':'528_N_oerstediiRh2',
'DQ646871':'522_N_oerstediiRh3',
'L78080':'520_Manduca_sexta',
'AF385331':'515_Spodoptera_exigua',
'AF385330':'510_Galleria_mellonella',
'AB007423':'520_Papilio_xuthusRh1',
'AB007424':'520_P_xuthusRh2',
'AB007425':'575_P_xuthusRh3',
'AB177984':'540_Pieris_rapae',
'AF385333':'530_Vanessa_cardui',
'AF385332':'510_Junonia_coenia',
'AF126750':'570_Heliconius_erato',
'AF126753':'550_Heliconius_sara',
'AF484249':'560_Bicyclus_anynana',
'U32502':'510_Camponotus_abdominalis',
'U32501':'510_Cataglyphis_bombycinus',
'U26026':'529_Apis_mellifera',
'AY485301':'529_Bombus_terrestris',
'AY572828':'553_Osmia_rufa',
'X80071':'520_Schistocerca_gregaria',
'X71665':'515_Sphodromanti_ssp',
'D50583':'480_Hemigrapsus_sanguineus',
'Z86118':'508_Drosophila_melanogasterRh6',
'AH001026':'478_D_melanogasterRh1',
'M58334':'490_Calliphora_erythrocephalaRh1',
'M12896':'420_D_melanogasterRh2',
'X80072':'430_S_gregaria',
'AD001674':'450_M_sexta',
'AB028217':'460_P_xuthusRh4',
'AF004168':'439_A_mellifera',
'U67905':'437_D_melanogasterRh5',
'AF004169':'353_A_mellifera',
'AF042788':'360_C_abdominalis',
'AF042787':'360_C_bombycinus',
'L78081':'357_M_sexta',
'AB028218':'P_xuthus_Rh5',
'AH001040':'375_D_melanogasterRh4',
'M17718':'345_D_melanogasterRh3',
'AH001149':'Bostaurus_rhodopsin'
}


InFileName= 'seq_acession.fasta' #is still only a string
InFile= open(InFileName,'r')

OutFile=open('newnames.fasta','w')


for Acession in InFile:
	if '>' in Acession:
		#print (Acession)
		#print (Acession.replace ('\n',''))
		key= (Acession.replace ('\n','').replace('>',''))
		#print (key)
		
		NewHeader='>'+ AcessDict[key]+'\n'
		NewHeader=NewHeader.replace(key,'')
		print (NewHeader)
		OutFile.write(NewHeader)
	else:
		print (Acession) 
		OutFile.write(Acession)



		
		#print ('Header is {}'.format (Acession, AcessDict [key]))


InFile.close()
OutFile.close()

