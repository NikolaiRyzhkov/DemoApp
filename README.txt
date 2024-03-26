Project description:
    The application counts the number of lines in a text file.
    To use the application you must register and confirm your email.

    Stack:
        Framework: Django
        Database: PostgresSQL
        Cache: Redis
        User registration: Email
        User authorization: JWT
        Distributed tasks: Redis+Celery


Deploy app:
    To run the application need a launch environment that supports docker

    1 Need to fill in the environment variables in DemoApp/.env for the database and smtp server
    2 Build and run a docker container:
        1 docker compose build
        2 docker compose up

Using the app:
    url: 127.0.0.1:8000/graphql/

    1 User registration:
        mutation CreateUser {
            createUser(email: your_email, password: your_pass, username: your_username) {
                token
                refreshToken
            }
        }

    2 Email confirmation:
        1 Get code:
            query EmailVerificationCode2 {
                emailVerificationCode
            }

        2 Confirm email:
            mutation ConfirmationEmail {
                confirmationEmail(code: code_from_your_email) {
                    info
                }
            }

    2 Get refresh token and token by username and pass:
        mutation TokenAuth {
            tokenAuth(username: your_username, password: your_pass) {
                payload
                refreshExpiresIn
                token
                refreshToken
            }
        }

    3 Get refresh token and token by refresh token
        mutation RefreshToken {
            refreshToken(refreshToken: your_refresh_token) {
                payload
                refreshExpiresIn
                token
                refreshToken
            }
        }

    4 Upload file:
        To download a file you must be an authorized user
        Headers:
            Authorization: Bearer your_token
            map: {"0": ["variables.file"]}
            0: your_txt_file
            operation:
                {"query":
                    "mutation UploadTxtFile($file: Upload!){
                        uploadTxtFile(file: $file) {
                            txtFile{id},
                        }
                    }",
                "variables": {
                    "file": null
                    }
                }

    5 Get info about last txt file by id or last upload file:
        1 by id:
            query TxtFileInfo {
                txtFileInfo(idTxtFile: txt_file_id) {
                    id
                    numberOfLines
                }
            }

        2 last file:
            query TxtFileInfo {
                txtFileInfo {
                    id
                    numberOfLines
                }
            }