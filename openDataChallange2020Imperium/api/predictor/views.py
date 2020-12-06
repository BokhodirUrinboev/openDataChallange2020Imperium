import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from openDataChallange2020Imperium.api.predictor.serializers import TAMSAMSOMSerializer
from openDataChallange2020Imperium.settings import OPEN_DATA_URL, OPEN_DATA_ACESS_KEY


class TAMSAMSOMAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def post(self, request, format=None):
        serializer = TAMSAMSOMSerializer(data=request.data)
        tam_population = 0
        sam_population = 0
        som_population = 0
        data = {}
        if serializer.is_valid():
            # region
            r = requests.get(OPEN_DATA_URL + '/dataset/11900/version/26671?access_key=' + OPEN_DATA_ACESS_KEY,
                             auth=('user', 'pass'))
            data = json.dumps(r.json())
            if 'region' in serializer.data.keys():
                for id in serializer.data['regions']:
                    for d in data:
                        if id == int(d['id']):
                            tam_population += int(d['G4'])
                        break
            else:
                tam_population = int(data[1]['G4'])
            sam_population = tam_population
            som_population = tam_population

            # education
            if 'education' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13054/version/28368?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())
                for d in data:
                    if serializer.data['education'] == int(d['id']):
                        som_population = som_population*d['G4']

            # has_computer
            if 'has_computer' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13051/version/28365?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())
                som_population = som_population*int(data[0]['G4'])

            # has_phone
            if 'has_phone' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13050/version/28364?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())
                som_population = som_population*int(data[0]['G4'])

            # has_internet
            if 'has_internet' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13049/version/28363?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())
                som_population = som_population*int(data[0]['G4'])

            # can_internet
            if 'can_internet' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13047/version/28361?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())
                sam_population = sam_population*int(data[0]['G4'])

            # has_house
            if 'has_house' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13045/version/28359?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())
                som_population = som_population*int(data[0]['G4'])

            # has_under_16 & no_of_children
            if 'has_under_16' in serializer.data.keys() or  'no_of_children' in serializer.data.keys():
                r = requests.get(OPEN_DATA_URL + '/dataset/13039/version/28365?access_key=' + OPEN_DATA_ACESS_KEY,
                                 auth=('user', 'pass'))
                data = json.dumps(r.json())

                if 'has_under_16' in serializer.data.keys():
                    # has_under_16
                    som_population = som_population*int(data[2]['G4'])
                    # has_under_16 no
                    som_population = som_population*int(data[3]['G4'])

                if 'no_of_children' in serializer.data.keys():
                    som_population = som_population*int(data[serializer.data['no_children']+4])['G4']

            data = {
                "TAM": tam_population,
                "SAM": sam_population,
                "SOM": som_population,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        pass