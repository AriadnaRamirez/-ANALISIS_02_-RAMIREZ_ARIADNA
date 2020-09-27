#Funcion que permite imprimir una lista de listas en formato de tabla
def imprime_top(lista_top,tema,titulo1,titulo2,titulo3,titulo4):
    print ("\n ",tema)
    print ("   ",titulo1," \t\t\t\t\t\t",titulo2," \t",titulo3," \t",titulo4," \n    --------------------------------------------------------------------------------------")    
    Tabla="""   {}"""
    Tabla = (Tabla.format('\n   '.join(" {:<35} {:<10}   ${:<20,}  {}".format(*fila)
    for fila in lista_top)))        
    print (Tabla)    
    
#Funcion que ordena las rutas de operacion por numero de usos o por el costo de operacion total de uso
def top_10_rutas(rutas_corto,rutas_completo,rutas_con_costo):
    rutas_orden,rutas_top10_operaciones,rutas_top10_costo=[],[],[]   
    
    for ruta in rutas_corto:        
        repeticion=rutas_completo.count(ruta)            
        costo=0                           
        for precio in rutas_con_costo:
            if ruta==precio[0]:                    
                costo+=int(precio[1])       
        rutas_orden.append([ruta,repeticion,costo," "])   
            
    rutas_orden_operaciones = sorted(rutas_orden, key=lambda ruta : ruta[1])
    rutas_orden_costo = sorted(rutas_orden, key=lambda ruta : ruta[2])            
        
    for indice in range(1,11): 
        rutas_top10_operaciones.append(rutas_orden_operaciones[-indice])
        rutas_top10_costo.append(rutas_orden_costo[-indice])         
  
    imprime_top(rutas_top10_operaciones,"POR NUMERO DE OPERACIONES","Ruta       ","N. de op","Costo de operación"," ")    
    imprime_top(rutas_top10_costo,"POR COSTOS DESCENDENTE","Ruta       ","N. de op","Costo de operación"," ")


#funcion que ordena los transportes usdos en las operaciones, por numero de usos o por costo en orden descendente    
def top3_transportes(transportes_completo,transportes,transporte_con_costo):
    transporte_orden,transporte_top3,transporte_top3_costo=[],[],[]

    for transporte in transportes:        
        repeticion=transportes_completo.count(transporte)            
        costo=0                           
        for medio in transporte_con_costo:
             if transporte==medio[2]:                    
                 costo+=int(medio[1])       
        transporte_orden.append([transporte,repeticion,costo," "])   
                
    transporte_orden_operaciones = sorted(transporte_orden, key=lambda transporte : transporte[1])
    rutas_orden_costo = sorted(transporte_orden, key=lambda ruta : ruta[2])            
            
    for indice in range(1,4):
        transporte_top3.append(transporte_orden_operaciones[-indice])
        transporte_top3_costo.append(rutas_orden_costo[-indice])
        
    imprime_top(transporte_top3,"POR USO DE TRANSPORTE","Transporte","Usos","Costo de operación"," ")
    imprime_top(transporte_top3_costo,"POR USO DE TRANSPORTE","Transporte","Usos","Costo de operación"," ")  

#funcion que ordena los paises de interes por porcentaje de participacion en el costo total
def top80porciento_paises(paises_completo,paises,paises_con_costo):
    pais_orden,pais_top80,pais_top80_costo=[],[],[]
    costo_total,porcentaje,total_paises,porcentaje_comparar=0,0,0,0
    
    for pais in paises:        
        repeticion=paises_completo.count(pais)            
        costo=0                           
        for operacion in paises_con_costo:
              if pais==operacion[3]:                    
                  costo+=int(operacion[1])       
        pais_orden.append([pais,repeticion,costo])       
                
    for costo in pais_orden:
        costo_total+=costo[2]        
    for costo in pais_orden:           
        costo.append(round(((costo[2]/costo_total)*100),2))
        porcentaje+=costo[3]      
            
    paises_orden_operaciones = sorted(pais_orden, key=lambda transporte : transporte[3],reverse=True)
    paises_orden_costo = sorted(pais_orden, key=lambda ruta : ruta[3])       

    for indice in paises_orden_operaciones:         
        if porcentaje_comparar<=80:
            porcentaje_comparar+=round((float(indice[3])),1)
            pais_top80.append(indice)           
    print("El valor total es: ${:<20,}".format(costo_total))    
    imprime_top(pais_top80,"PAISES QUE APORTAN EL 80% DE GANANCIAS","Pais      ","Usos","    Costo de operación","% de aportación")    
   
    
#Apertura del archivo csv
import csv
with open ("synergy_logistics_database.csv", "r") as base_de_datos:
    lector = csv.DictReader (base_de_datos)   #Almacena los datos del archivo csv en un diccionario 
    
    #Variables para exportaciones
    rutas_exportacion,rutas_exportacion_precio,paises_exportan,transporte_exportacion=[],[],[],[]
    
    #Variables para importaciones
    rutas_importacion,rutas_importacion_precio,paises_importan,transporte_importacion=[],[],[],[]    
    
    #Genera litas independientes, clasificados en importaciones y expotaciones.
        # Listas:
            #*Lista que almacena ruta, costo y medio detransporte
            #*Lista que almacena unicamnete rutas 
            #*Lista que almacena unicamente el pais de origen o destino segun el interes del analisis
            #*Lista que alamcena los medios de trasporte utilizados
        
    for registro in lector:       
        if registro["direction"] == "Exports":             
            rutas_exportacion_precio.append([registro["origin"] +"-"+ registro["destination"],registro["total_value"],registro["transport_mode"],registro["origin"]])
            rutas_exportacion.append((registro["origin"] +"-"+ registro["destination"]))             
            paises_exportan.append(registro["origin"])            
            transporte_exportacion.append(registro["transport_mode"])
            rutas_exportacion_corto=list(set(rutas_exportacion))
            paises_exportan_corto=list(set(paises_exportan))
            transporte_exportacion_corto=list(set(transporte_exportacion))           
            
        else:   
            rutas_importacion_precio.append([registro["origin"] +"-"+ registro["destination"],registro["total_value"],registro["transport_mode"],registro["destination"]])
            rutas_importacion.append((registro["origin"] +"-"+ registro["destination"]))
            paises_importan.append(registro["destination"])
            transporte_importacion.append(registro["transport_mode"])
            rutas_importacion_corto=list(set(rutas_importacion)) 
            paises_importan_corto=list(set(paises_importan))
            transporte_importacion_corto=list(set(transporte_importacion))            
#Fin de la creacion de listas y del uso del archivo csv
    
#--------------------------------------CONSIGNA 1-------------------------------------------------
print("C O N S I G N A   1 ")            
print("➞RUTAS DE EXPORTACIÓN ") 
#Llama a la funcion que imprime una tabla con las rutas que tienen mayor numero de operaciones y otra con las rutas que generan mayores ganancias para exportaciones   
top_10_rutas(rutas_exportacion_corto,rutas_exportacion,rutas_exportacion_precio) #Ejecuta la funcion top_10_rutas, para las listas de exportacion
print(" ")
print("➞RUTAS DE IMPORTACIÓN ")
#Llama a la funcion que imprime una tabla con las rutas que tienen mayor numero de operaciones y otra con las rutas que generan mayores ganancias para importaciones   
top_10_rutas(rutas_importacion_corto,rutas_importacion,rutas_importacion_precio)#Ejecuta la funcion top_10_rutas, para las listas de importacion
    
#--------------------------------------CONSIGNA 2-------------------------------------------------
print(" ")
print("C O N S I G N A   2 ")
print("➞RUTAS DE EXPORTACIÓN ") 
#Llama a la funcion que imprime una tabla con los transportes que tienen mayor numero de operaciones y otra con los transportes que generan mayores ganancias para exportaciones
top3_transportes(transporte_exportacion,transporte_exportacion_corto,rutas_exportacion_precio)#Ejecuta la funcion top3_transportes, para las listas de exportacion
print(" ")
print("➞RUTAS DE IMPORTACIÓN ")
#Llama a la funcion que imprime una tabla con los transportes que tienen mayor numero de operaciones y otra con los transportes que generan mayores ganancias para importaciones
top3_transportes(transporte_importacion,transporte_importacion_corto,rutas_importacion_precio)#Ejecuta la funcion top3_transportes, para las listas de importacion

#---------------------------------------CONSIGNA 3------------------------------------------------
print(" ")
print("C O N S I G N A   3 ")      
print("➞RUTAS DE EXPORTACIÓN ")
#Llama a la funcion que imprime los paises que aportan el 80% de los ingresos por exportacion
top80porciento_paises(paises_exportan,paises_exportan_corto,rutas_exportacion_precio)
print(" ")
print("➞RUTAS DE IMPORTACIÓN ")
#Llama a la funcion que imprime los paises que aportan el 80% de los ingresos por importacion
top80porciento_paises(paises_importan,paises_importan_corto,rutas_importacion_precio)













