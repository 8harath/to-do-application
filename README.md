# Simple Todo List Application

A lightweight, easy-to-use todo list application built with HTML, CSS, and JavaScript, with an optional Python Flask backend.

![Todo List App](screenshots/todo-app.png)

## Features

- ✨ Create, read, update, and delete todos
- 🔍 Filter tasks by status (All, Active, Completed)
- 💾 Local storage persistence
- 🎨 Clean and responsive design
- ⌨️ Keyboard shortcuts (Enter to add todo)
- 🔄 Optional Python backend for server-side storage

## Live Demo

Check out the live demo: [Simple Todo List](https://8harath.github.io/to-do-application)

## Getting Started

### Frontend Only Version

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple-todo-list.git
cd simple-todo-list
```

2. Open `index.html` in your browser or use a simple HTTP server:
```bash
# Using Python
python -m http.server 8000

# Then visit http://localhost:8000 in your browser
```

### With Python Backend

1. Install required packages:
```bash
pip install flask flask-cors
```

2. Start the Flask server:
```bash
python app.py
```

3. Start the frontend server:
```bash
python -m http.server 8000
```

4. Visit `http://localhost:8000` in your browser

## Project Structure

```
simple-todo-list/
├── index.html          # Main HTML file
├── style.css          # Styles
├── script.js          # Frontend JavaScript
├── app.py            # Python backend (optional)
├── README.md         # Project documentation
├── LICENSE           # MIT license
└── screenshots/      # Project screenshots
    └── todo-app.png  # Main app screenshot
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Icons and design inspiration from [Material Design](https://material.io/)
- Built with vanilla JavaScript and CSS
- Flask for the backend API

## Contact

Your Name - [@8harath](https://x.com/8harath_k)

Project Link: [https://github.com/8harath/to-do-application](https://github.com/8harath/to-do-application)
