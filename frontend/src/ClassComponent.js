import React from "react";

export default function ClassComponent(props) {
    const [clickedClass, setClassClicked] = React.useState(-1);
    if (clickedClass !== -1) {
        for (var i = 0; i < props.classObject.length; i++) {
            if (props.classObject[i].id === clickedClass) {

                return (
                    <div>
                        <h1>Class Clicked</h1>
                    </div>
                )
            }
        }
        return (
            <div>
                <h1>Error! Data for the clicked class could not be found. </h1>
                <p>Go back to classes overview:</p>
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