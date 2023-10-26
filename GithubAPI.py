from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your GitHub username
github_username = "ketanskanade"

# Replace with your GitHub Personal Access Token (Generate one from GitHub)
github_token = "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"

# GitHub Gists API endpoint
github_api_url = f"https://api.github.com/users/{github_username}/gists"

@app.route('/')
def get_gists():
    try:
        # Send a GET request to GitHub API to fetch user's gists
        response = requests.get(github_api_url, headers={'Authorization': f'token {github_token}'})

        if response.status_code == 200:
            # Parse the JSON response
            gists = response.json()

            # Extract the gist information you want to include in the response
            gist_info = []

            for gist in gists:
                gist_data = {
                    "id": gist['id'],
                    "description": gist['description'],
                    "url": gist['html_url'],
                }
                gist_info.append(gist_data)

            return jsonify(gist_info)

        else:
            return f"Failed to fetch Gists from GitHub API. Status Code: {response.status_code}", 500

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
