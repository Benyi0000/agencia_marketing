import { connect } from 'react-redux'

function Navbar() {
    return(
        <nav className='w-full py-10 shadow-md fixed'>
            <li>
                <ul>Opcion 1</ul>
            </li>
        </nav>)    
}

const mapStateToProps = () => ({ });
  

export default connect(mapStateToProps,{
 })(Navbar);