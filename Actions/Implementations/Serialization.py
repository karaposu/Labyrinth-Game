from Actions.Services.ISerialization import   ILabyrinthSerializer

class  Serializator(ILabyrinthSerializer):

    def Serialize(self, OBJ):


        if isinstance(OBJ, complex):
            # just the key of the class name is important, the value can be arbitrary.
            return {OBJ.__class__.__name__: True, "real": OBJ.real}
        else:
            raise TypeError(f"Object of type '{OBJ.__class__.__name__}' is not JSON serializable")

        zJSON = json.dumps(z, default=encode_complex)



    def Deserialize(self, OBJ):
        pass
