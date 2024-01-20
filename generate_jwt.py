import jwt
import datetime
import uuid

user = ''
connectedAppClientId = ''
connectedAppSecretKey = ''
connectedAppSecretId = ''

token = jwt.encode(
	{
		"iss": connectedAppClientId,
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": user,
		"scp": ["tableau:views:embed"],
		"Region": "East"
	},
		connectedAppSecretKey,
		algorithm = "HS256",
		headers = {
		'kid': connectedAppSecretId,
		'iss': connectedAppClientId
        }
  )

print(token)