import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addHelper } from '../../actions/helpers'

export class Form extends Component {
    state = {
        name: '',
        surname: '',
        zipcode: '',
        email: ''
    }

    static propTypes = {
        addHelper: PropTypes.func.isRequired
    };

    onChange = e => this.setState({ [e.target.name]: e.target.value });

    onSubmit = e => {
        e.preventDefault();
        const { name, surname, email, zipcode } = this.state;
        const helper = { name, surname, email, zipcode };
        this.props.addHelper(helper);
        this.setState({
            name: '',
            surname: '',
            email: '',
            zipcode: ''
        });
        console.log('submit');
    }

    render() {
        const {name, surname, zipcode, email} = this.state;
        return (
            <div>
                <div className="card card-body mt-4 mb-4">
                    <h2>Add Helper</h2>
                    <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Name</label>
                        <input
                        className="form-control"
                        type="text"
                        name="name"
                        onChange={this.onChange}
                        value={name}
                        />
                    </div>
                    <div className="form-group">
                        <label>Surname</label>
                        <input
                        className="form-control"
                        type="text"
                        name="surname"
                        onChange={this.onChange}
                        value={surname}
                        />
                    </div>
                    <div className="form-group">
                        <label>Email</label>
                        <input
                        className="form-control"
                        type="email"
                        name="email"
                        onChange={this.onChange}
                        value={email}
                        />
                    </div>
                    <div className="form-group">
                        <label>Zip Code</label>
                        <textarea
                        className="form-control"
                        type="text"
                        name="zipcode"
                        onChange={this.onChange}
                        value={zipcode}
                        />
                    </div>
                    <div className="form-group">
                        <button type="submit" className="btn btn-primary">
                        Submit
                        </button>
                    </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default connect(null, { addHelper })(Form)