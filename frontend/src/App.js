import React,{Component} from 'react';
import axios from 'axios';

class App extends Component {
  state={
    todos: [],
  };
  componentDidMount() {
    this.getTodos();
  }
  getTodos() {
    axios
    .get('http://127.0.0.1:8000/api/')
    .then(res => {
      this.setState({todos: res.data});
    })
    .catch(err => {
      console.log(err);
    });

  }

  

  render() {
    return (
      <>
      <h1>Todo List</h1>
      <div className="todo-list">
        {this.state.todos.map(item => (
          <div key={item.id} className="todo-item">
            <h3>{item.title}</h3>
            <span>{item.body}</span>
            <p>Status: {item.completed ? "Completed" : "Not Completed"}</p>
            <p>Created At: {new Date(item.created_at).toLocaleString()}</p>
          </div>
        ))}
      </div>
      </>
    );
  }
}

export default App;
