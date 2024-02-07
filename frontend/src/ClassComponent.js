import React from "react";
import Student from "./Student.js";

export default function ClassComponent(props) {
    const [clickedClass, setClassClicked] = React.useState(-1);
    if (clickedClass !== -1) {
        const studentArray = props.classObject.student.map(currentStudent => {
            return <Student student={currentStudent} token={props.token} />
        })
        return (
            <div>
                <h1>Details of Class {props.classObject.className}</h1>
                {studentArray}
                <button onClick={() => setClassClicked(-1)}>Back</button>
            </div>
        )
    }
    else {
        return (
            <div className="classBox">
                <button onClick={() => setClassClicked(props.classObject.id)}>
                    <h3>{props.classObject.className}</h3>
                </button>
            </div>
        )
    }
}