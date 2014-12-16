'''
Created on Dec 11, 2014

@author: Lei Lu
'''
def executeAnalysis(visualizer_instance, ui):
    '''
    execute exploratory Analysis after receiving user input
    '''
    while True:
        ui.welcome()
        parameter = ui.options()
        if parameter == 1:
            visualizer_instance.unixvis_collisonsAndFatalities()
        elif parameter == 2:
            visualizer_instance.unixvis_vehicleTypes()
        elif parameter == 3:
            visualizer_instance.unixvis_contributingFactors()
        elif parameter == 4:
            visualizer_instance.unixvis_regressionVehicleXFatalities()

        if ui.finished():
            break
        

        
        
            
