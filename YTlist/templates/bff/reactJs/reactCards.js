{% load i18n static %}
{% verbatim %}

class AppCard extends React.Component {

constructor(){
    super()
    this.state ={

        n: "",
        TlinkStart: "https://twitter.com/intent/tweet?url=learMore&amp;text=Moore  ",
        TlinkEnd: "   Translation App ::: Plz visit philserme.com."
    }
    this.pll = this.pll.bind(this);
}


 pll(n){
 {% endverbatim %}
var s = "{% static "media/" %}"+n;
{% verbatim %}


document.getElementById('myAudio').src= s;
document.getElementById('myAudio').play();

}


  render() {



    return <li className="sm-6 md-4 lg-4 col">
    <i className="card  animated flipInX" >
    <b className="card-body" key={this.props.sound} onClick={() => this.pll(this.props.sound)}>

    <p className="card-title">{this.props.mr} </p>
    <p className="card-title">{this.props.fr} </p>
    <p className="card-title">{this.props.en} </p>
    <p className="card-title">{this.props.sp} </p>
<hr/>
    <div className="text-center">
    <div className="text-secondary">
        <a className="btn btn-sm share-twitter" target="_blank" href={this.state.TlinkStart + this.props.mr+" (moree) "+ this.props.fr+" (francais) " + this.props.en+" (english) " + this.props.sp+" (spanish) " + this.state.TlinkEnd}>
        <span className="fa fa-twitter"></span> Share
        </a>
    </div>

</div>


  </b>
  </i>

</li>;
  }

}

  {% endverbatim %}
