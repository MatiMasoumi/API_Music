import requests

class iTunesAPI: 
    """A class to interact with the iTunes Search ApI"""
    base_url="https://itunes.apple.com/search"

    def search_music(self,track_name):
        """
        search for music by track name.
        """
        params = {
            'term':track_name,
            'media':'music',
            'limit':10
            }
        try:
            reponse=requests.get(self.base_url,params=params)
            reponse.raise_for_status()
            data=reponse.json()
            return data.get('results',[])
        except requests.exceptions.RequestException as e:
            print(f'error while accessing iTunes API:{e}')
            return []
    
class MusicApp:
    """
    A user interface class for the iTunesAPI
    """

    def __init__(self):
        self.api=iTunesAPI()

    def run(self):
        """
        main loop for the aplication
        """
        print('welcom to the iTunes music search!')
        while True:
            track_name=input("\nEnter the name of the song to search(or 'exit' to quit):").strip()
            if track_name.lower() == 'exit':
                print('Goodbye!')
                break
            results = self.api.search_music(track_name)
            self.display_results(results)

    def display_results(self,results):
        """
        display the search results
        """
        if not results:
            print('No results found.pleace try again.')
            return
        print("\nsearch Results:")
        print("-" * 50)
        for index,result in enumerate(results,start=1):
            track_name=result.get('trackName', 'Unknow')
            artist_name=result.get('tartistName', 'Unknow')
            album_name=result.get('collection_name', 'Unknow')
            preview_url=result.get('previewUrl','No preview avaible')
            print(f'{index}.track:{track_name}')
            print(f'artist:{artist_name}')
            print(f'album:{album_name}')
            print(f'preview:{preview_url}')
            print("-" * 50)


if __name__ == "__main__":
    app=MusicApp()
    app.run()