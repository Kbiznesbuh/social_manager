def route_message(message):
    """
    Routes the incoming message to the appropriate handler based on the source.
    
    Args:
        message (dict): The incoming message containing source and content.
    
    Returns:
        str: Response message after processing.
    """
    source = message.get('source')
    
    if source == 'telegram':
        return handle_telegram_message(message)
    elif source == 'vk':
        return handle_vk_message(message)
    else:
        return "Unknown source"

def handle_telegram_message(message):
    """
    Handles messages coming from Telegram.
    
    Args:
        message (dict): The incoming Telegram message.
    
    Returns:
        str: Response message.
    """
    user_name = message.get('user_name')
    message_text = message.get('message_text')
    return f"Received from Telegram: {user_name}: {message_text}"

def handle_vk_message(message):
    """
    Handles messages coming from VK.
    
    Args:
        message (dict): The incoming VK message.
    
    Returns:
        str: Response message.
    """
    user_name = message.get('user_name')
    message_text = message.get('message_text')
    return f"Received from VK: {user_name}: {message_text}"