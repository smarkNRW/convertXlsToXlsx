#!/usr/bin/env python
# encoding: utf-8

# Author: Markus Saalmann
# Description: ie APP baut eine Verbindung zu einer Datenbank auf und führt eine Reihe von TSQL-Statements aus und Exportiert 
# das Ergebnis in eine CSV Datei.
#
#-----------------------------------------------------------------------------------------------------------------------------------------

#Importe für den SMTP Versand
import json
import pandas as pd
import argparse #ARGS parsen


# Project defined imports
#-----------------------------
#Konfiguration lesen
f = open('config.json')
config = json.load(f)

import sys
sys.path.append(config['LIB_PATH']) 
from libCore.libTrace import Trace #Bibliothek für ein zentrales Tracing

def ConvertXlsToXlsx(input_path, output_path):
    try:
        Trace(f'Lese: {input_path}','I')
        df = pd.read_excel(input_path, engine='xlrd')
    except Exception as e:
        Trace(f'Error: {e}','E')
    else:
        Trace(f'Schreibe: {output_path}','I')
        try:
            df.to_excel(output_path, index=False)
        except Exception as e:
            Trace(f'Error: {e}','E')
        Trace('Fertig!','I')

if __name__ == '__main__':
    Trace().activateTrace(InformationTypes=config['LOG_InformationTypes'],WriteOnlyToLogFile=config['LOG_WriteOnlyToLogFile'], LogFilePath=config['LOG_PATH'])
    Trace(f"********* APP: {config['APP_NAME']} ******** Version: {config['APP_VERSION']} ***************")
    
    #ARG Parser initialisieren
    parser = argparse.ArgumentParser(
        prog = config['APP_NAME'],
        description = 'Das Script konvertiert eine XLS Datei in eine XLSX-Datei'
       )
    parser.add_argument('-i', dest='inputfile', required = True, )
    parser.add_argument('-o', dest='outputfile', required = True, )
    
    #effektive Argumente ermitteln
    args = parser.parse_args()
    
    input_path = args.inputfile
    output_path = args.outputfile
    
    if input_path and output_path: 
        ConvertXlsToXlsx(input_path=input_path, output_path=output_path)
    
    