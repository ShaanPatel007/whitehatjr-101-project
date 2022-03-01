import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_data(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'rMvJfnPerY4AAAAAAAAAAdlYVt73RwFsqrAjNLHQod8C6ABxYbVjyCNUoDNIWwX-'
    TransferFile = TransferData(access_token)

    file_from = input("Enter the file to transfer:- ")
    file_to = input("Enter the file to upload in dropbox:- ")

    TransferFile.upload_data(file_from,file_to)
    print('file transfered')

main()