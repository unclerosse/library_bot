import requests

class G_books:
    URL = 'https://www.googleapis.com/books/v1/volumes'
    
    @classmethod
    def get_books(cls, question: str, results: int=5):
        params = {
            'q': question,
            'maxResults': results
        }
        r = requests.get(cls.URL, params=params)

        return r.json()

    @classmethod
    def choose_book(cls, all_data, *params) -> dict:
        books = []
        
        for i in range(len(all_data['items'])):
            data = all_data['items'][i]
            volume_info = data['volumeInfo']        
            book = {'gid': data['id']}

            for el in params:
                match el:
                    case 'title':
                        book['title'] = volume_info['title']
                    case 'subtitle':
                        book['subtitle'] = volume_info['subtitle']
                    case 'authors':
                        book['authors'] = volume_info['authors']
                    case 'publisher':
                        book['publisher'] = volume_info['publisher']
                    case 'description':
                        book['description'] = volume_info['description']
                    case 'pages':
                        book['pages'] = volume_info['pageCount']
                    case 'image_link':
                        book['image_link'] = volume_info['imageLinks']['thumbnail']
                    case 'buy_link':
                        book['buy_link'] = data['saleInfo']['buyLink']
                    case 'price':
                        book['price'] = str(data['saleInfo']['listPrice']['amount']) \
                            + data['saleInfo']['listPrice']['currencyCode']
            books.append(book)
        
        return books
        