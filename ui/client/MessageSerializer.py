from json import JSONEncoder

class MessageSerializer(JSONEncoder):

    def default(self, object: object) -> object:

        object_dict = object.__dict__

        receiver_id = object_dict.get("receiver_id")

        if not receiver_id:
            raise KeyError(receiver_id)
        
        text = object_dict.get("text")
        
        if not text:
            raise KeyError(text)
        
        return { "receiver_id" : receiver_id, "text" : text }
    