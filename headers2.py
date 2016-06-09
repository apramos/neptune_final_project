#! /usr/bin/env python
import re 

AcessDict={	
'X56788':'494 Loligo forbesi',
'AY450853':'493 Loligo pealii',
'Z49108':'499 Loligo subulata',
'AF000947':'492 Sepia officinalis',
'X70498':'480 Todarodes pacificus',
'X07797':'475 Enteroctopus dofleini',
'L03781':'520 Limulus polyphemus',
'L03782':'530 L polyphemus',
'DQ852576':'487 Euphausia superba',
'DQ852587':'515 Homarus gammarus',
'AF003544':'526 Cambarellus shufeldtii',
'AF003543':'529 Cambarus ludovicianus',
'AF003545':'530 Orconectes virilis',
'AF003546':'522 Procambarus milleri',
'S53494':'533 Procambarus clarkii',
'DQ852573':'496 Archaeomysis grebnitzkii',
'DQ852581':'512 Holmesimysis costata',
'DQ852591':'501 Mysis diluviana',
'DQ852592':'520 Neomysis americana',
'DQ646869':'489 Neogonodactylus oerstediiRh1',
'DQ646870':'528 N oerstediiRh2',
'DQ646871':'522 N oerstediiRh3',
'L78080':'520 Manduca sexta',
'AF385331':'515 Spodoptera exigua',
'AF385330':'510 Galleria mellonella',
'AB007423':'520 Papilio xuthusRh1',
'AB007424':'520 P xuthusRh2',
'AB007425':'575 P xuthusRh3',
'AB177984':'540 Pieris rapae',
'AF385333':'530 Vanessa cardui',
'AF385332':'510 Junonia coenia',
'AF126750':'570 Heliconius erato',
'AF126753':'550 Heliconius sara',
'AF484249':'560 Bicyclus anynana',
'U32502':'510 Camponotus abdominalis',
'U32501':'510 Cataglyphis bombycinus',
'U26026':'529 Apis mellifera',
'AY485301':'529 Bombus terrestris',
'AY572828':'553 Osmia rufa',
'X80071':'520 Schistocerca gregaria',
'X71665':'515 Sphodromanti ssp',
'D50583':'480 Hemigrapsus sanguineus',
'Z86118':'508 Drosophila melanogasterRh6',
'AH001026':'478 D melanogasterRh1',
'M58334':'490 Calliphora erythrocephalaRh1',
'M12896':'420 D melanogasterRh2',
'X80072':'430 S gregaria',
'AD001674':'450 M sexta',
'AB028217':'460 P xuthusRh4',
'AF004168':'439 A mellifera',
'U67905':'437 D melanogasterRh5',
'AF004169':'353 A mellifera',
'AF042788':'360 C abdominalis',
'AF042787':'360 C bombycinus',
'L78081':'357 M sexta',
'AB028218': 'P xuthusRh5',
'AH001040':'375 D melanogasterRh4',
'M17718':'345 D melanogasterRh3',
'AH001149': 'Bostaurus rhodopsin'
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

