import GEOparse

def get_geneID(geo_id, gsms_id, gpls_id):
    gse = GEOparse.get_GEO(geo=geo_id, destdir="./")
    
    #Get all GSMS(samples) info:
    gse.phenotype_data
    
    #Use sample name to retrieve corresponding data:
    gse.gsms[gsms_id].table
    
    #PLatform info
    probeset = gse.gpls[gpls_id].table
    columns = probeset.columns
    
    return probeset[['ID', 'GB_LIST', 'Gene Title', 'Gene Symbol']], columns

