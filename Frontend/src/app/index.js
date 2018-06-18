import React, { Component } from "react"
import { render } from "react-dom"
/*import { Rating } from 'semantic-ui-react'
import "semantic-ui-css/semantic.css";*/
import { Button, } from 'semantic-ui-react'
import { Icon,Card,Image,Grid } from 'semantic-ui-react'

import './index.css'

class MyComponent extends Component {
  constructor(){
    super();
    this.state = {
      items:[]
    }
  }
  componentDidMount() {
    this.getItem();
 
  }
  getItem() {
    fetch('http://localhost:8000/api/list/')
    .then(results => results.json())
    .then(results => this.setState({items:results}));
  }
  render(){
    return (
      <div>
        <nav className="nav-bar">
          <div className="padding">
            <Button size="mini" floated="right">Sign up</Button>
            <Button size="mini" floated="right">Login in</Button>
          </div>
        </nav>
        <h1>Hello from My Component</h1>
        <h1>Hello from My Component</h1>
        <ul>
          {this.state.items.map(function(item,index){

            return (
              
                <Card.Group centered itemsPerRow={4}>  
                  <Card>
                    <Image src={item.image}/>
                    <Card.Content>
                      <Card.Header>{item.title}</Card.Header>
                      <Card.Description>{item.description}</Card.Description>
                    </Card.Content>
                    <Card.Content extra>
                      <Button animated='vertical'color='yellow'size='mini'>
                        <Button.Content hidden>Shop</Button.Content>
                        <Button.Content visible>
                          <Icon name='shop'/>
                        </Button.Content>
                      </Button>
                    </Card.Content>
                    </Card>
                  </Card.Group>
              
              
              
              
            )
          
            
          })}
        </ul>
        <i class="shopping cart icon"size="large"></i>
       
    </div>
    )




  }
}
/*<Grid columns={2} padded='horizontally' centered>

.articles{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 30px;
}



<Grid columns={3}>
    <Grid.Row>
      <Grid.Column>
        <Image src='/assets/images/wireframe/paragraph.png' />
      </Grid.Column>
      <Grid.Column>
        <Image src='/assets/images/wireframe/paragraph.png' />
      </Grid.Column>
    </Grid.Row>





*/
   

/*class MyComponent extends Component {
 constructor(props)  {
     super(props);
     this.state = {}
 }
 componentDidMount{
   this.getItem();

 }
 getItem(){
   fetch(http://localhost:8000/api/list/)
   .then(results => result.json())
   .then({results}) => console.log(results))
 }
 handleRate(e, { rating, maxRating }){ this.setState({ rating, maxRating })}

  render() {
    return (
      <div>
        <Rating maxRating={5} onRate={this.handleRate.bind(this)} />
        <pre>{JSON.stringify(this.state, null, 2)}</pre>
      </div>
    )
  }
}
<Card>
    <Image src='/assets/images/avatar/large/matthew.png' />
    <Card.Content>
      <Card.Header>Matthew</Card.Header>
      <Card.Meta>
        <span className='date'>Joined in 2015</span>
      </Card.Meta>
      <Card.Description>Matthew is a musician living in Nashville.</Card.Description>
    </Card.Content>
    <Card.Content extra>
      <a>
        <Icon name='user' />
        22 Friends
      </a>
    </Card.Content>
  </Card>


*/

render(<MyComponent />, document.getElementById("root"));



