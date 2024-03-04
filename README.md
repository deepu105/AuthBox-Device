AuthBox Device UI

# Get Started
## Setup your Auth0 tenant and application
- Create a free account on [auth0.com](https://auth0.com) if you don't have one already
- Create a new "native application" called "Authbox" in your Auth0 dashboard
- Add `http://localhost:5173` and `authbox.local:5173` as allowed callback URLs, allowed logout URLs and allowed web origins. (If you're not using Vite or have changed the port, make sure to use your developement URL)
- Enable the "Allow Cross-Origin Authentication" toggle
- Under Advanced settings > Grant Types, make sure "Device Code" is enabled

## Run the application
- run `npm install` to install all dependencies
- copy the `.env.sample` file to `.env`
- Add your Auth0 application's client ID and Domain to the `.env` file
- run `npm run dev -- --host` to start a development server

## Run the python hardware interface
In order to interact with the AuthBox hardware, a python interface is provided. This server listens to HTTP requests to interact with the hardware using the serial port.

- run `sudo apt install flask` to install flask
- run `flask --app hardware/esp32interface.py run --host=0.0.0.0` to launch the hardware interface
