### READ ME
This app is deployed for the Mochi Health tech screening.
The app is designed to log a mood and note from a user and display today's aggregated data.

One known issue is that the connection can't write to a public sheet. Writing secrets in order to use a private sheet in conjunction with a service account resulted in the app not recognizing that there were any secrets, thereby preventing me from using a private sheet at all. I tried trouble shooting for a few hours but to no avail. Whenever I would try to use st.secrets it would give me the error that there were no secrets found, despite me adding secrets to the deployed app and the toml format was not giving any errors.