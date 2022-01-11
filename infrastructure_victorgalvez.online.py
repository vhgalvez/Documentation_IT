from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve
from diagrams.programming.framework import Django
from diagrams.programming.flowchart import Database
from diagrams.programming.framework import Vue
from diagrams.programming.framework import FastAPI
from diagrams.programming.framework import Flutter
from diagrams.onprem.database import PostgreSQL
from diagrams.generic.os import Android
from diagrams.generic.os import IOS


with Diagram("ARQUITECTURA APLICACION", show=False, filename="ARQUITECTURA_APLICACION", direction="LR"):

    with Cluster("ARQUITECTURA APLICACION"):

        # download the icon image file
        chrome_url = "https://cdn.icon-icons.com/icons2/1365/PNG/512/browser_89380.png"
        chrome_icon = "chrome.png"
        urlretrieve(chrome_url, chrome_icon)
        

        # download the icon image file
        api_url = "https://img.icons8.com/wired/64/000000/api-settings.png"
        api_icon = "api.png"
        urlretrieve(api_url, api_icon)

        # API = Custom("API", api_icon)
        # Database_server = Database("Database")


        fast = FastAPI("FastAPI")
        chrome = Custom("HTTP Request", chrome_icon)
        PostgreSQL_server = PostgreSQL("PostgreSQL")
        Android_device = Android("Android")
        IOS_device = IOS("IOS")
        Vue_app = Vue("Vue")
        Flutter_server = Flutter("Flutter")
        
        #fast >> PostgreSQL_server  
        #fast >> PostgreSQL_server

        
        fast >> Flutter_server 
        fast >> Vue_app
        chrome >> fast

        

        Flutter_server >> Android_device
        Flutter_server >> IOS_device

        PostgreSQL_server >> fast  
        PostgreSQL_server >> fast
        
    

    # ARQUITECTURA APLICACION 
    # @victorgalvez
    # victorgalvez.online
    # vhgalvez@gmial.com
    # license: MIT  
    # version: 1.0.0
    # date: 2020-05-01
    # language: python3
    # description: ARQUITECTURA APLICACION

