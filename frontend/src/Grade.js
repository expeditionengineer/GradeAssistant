import React from "react";
import axios from "axios";

export default function Grade(props) {
    
    // function showChildInputFields() {
    //     console.log("clicked")
    // }
    const [details, setDetails] = React.useState(false);
    function toggleDetails() {
        setDetails(!details);
    }
    function addChild(gradeId) {
        axios.post('http://127.0.0.1:8000/addGrade/', {
            points: null,
            weight: null,
            parent: gradeId,
        }, {headers: {
            Authorization: `Token ${props.token}`
        }
    },)
        .then(response => {
            console.log(response.data);
            if (response.data.status === "created") {
                console.log("Created child grade!");
            }
        })
        .catch(error => {
            console.error(error);
            // Handle the error here
        });   
    }

    return (
        <div className="grade">
            <button onClick={toggleDetails}>
            <input 
                value={props.grade.points} 
                type="text" 
                // onClick={showChildInputFields}
            />
            </button>
            {details && (
            <div className="details">
                <li>
                    <ul>
                        Change Weight: <input value={props.grade.weight} type="text" />
                    </ul>
                    <ul>
                        <button onClick={() => addChild(props.grade.id)}>Add Child</button>
                    </ul>
                </li>
            </div>
            )}
        </div>
    )
}