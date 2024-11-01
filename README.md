# PotOS - Digital Twin and Control Web Interface for ROV

**PotOS** is a web-based interface developed by Yazid Marzuk to visualize and control the digital twin of the Remotely Operated Underwater Vehicle (ROV). The platform integrates real-time sensor data, live video feeds, and control capabilities, providing comprehensive monitoring and command over the ROV’s operations.

## Features

- **Digital Twin Visualization**: View a 3D representation of the ROV and its underwater environment in real time.
- **Real-Time Sensor Data**: Access live sensor data, including depth, orientation, temperature, and environmental variables, directly within the web interface.
- **Video and Sonar Feeds**: Display real-time video from the ROV’s camera, as well as data from Side Scan Sonar and Navigational Sonar, for an immersive view of the underwater environment.
- **Obstacle Detection**: Visualize obstacles detected by the ROV’s sensors to assist in navigation and maneuvering.
- **NMEA Command Interface**: Send NMEA commands to control various ROV functions and adjust settings as needed.
- **ROS Integration**: Backend built on ROS, providing a reliable and extensible framework for data streaming and command handling.
- **Flask Web Interface**: Intuitive and user-friendly Flask-based frontend for accessible ROV operation and monitoring.

## Project Structure

- `server.py` - Manages the Flask backend and ROS-based data streaming.
- `frontend/` - Web interface for digital twin visualization, sensor monitoring, and command input.
- `control/` - Contains modules for sending NMEA commands and controlling the ROV’s systems.
- `config/` - Configuration files for ROS, network settings, and data handling parameters.

## Contributing

We welcome contributions to enhance PotOS’s features and usability. Please review `CONTRIBUTING.md` for guidelines on issue submissions, pull requests, and our development process.

## License

This project is licensed under the MIT License. See the `LICENSE` file for further details.
