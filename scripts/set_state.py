#==================================================================================================
#  python_scripts/set_state.py 
#  https://community.home-assistant.io/t/how-to-manually-set-state-value-of-sensor/43975/9
#==================================================================================================

#--------------------------------------------------------------------------------------------------
# Set the state or other attributes for the entity specified in the Automation Action
#--------------------------------------------------------------------------------------------------

inputEntity = data.get('entity_id')
if inputEntity is None:
    logger.warning("===== entity_id is required if you want to set something.")
else:    
    inputStateObject = hass.states.get(inputEntity)
    inputState = inputStateObject.state
    inputAttributesObject = inputStateObject.attributes.copy()

    for item in data:
        newAttribute = data.get(item)
        logger.debug("===== item = {0}; value = {1}".format(item,newAttribute))
        if item == 'entity_id':
            continue            # already handled
        elif item == 'state':
            inputState = newAttribute
        else:
            inputAttributesObject[item] = newAttribute
        
    hass.states.set(inputEntity, inputState, inputAttributesObject)