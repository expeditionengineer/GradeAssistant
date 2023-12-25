import React, { useEffect } from "react"
import axios from "axios"
import ClassComponent from "./ClassComponent";

axios.defaults.xsrfCookieName = "csrftoken";
axios.default.xsrdHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;
export default function Dashboard(props) {
    var classArray =[]
    const [user, setUser] = React.useState("");
    const [classForUser, setClass] = React.useState();
    const [grade, setGrade] = React.useState();
    const [student, setStudent] = React.useState();

    useEffect( async () => {
        const response = await axios.get("http://127.0.0.1:8000/dashboard/", {
            headers: {
                Authorization: `Token ${props.token}`
            }
        });
        setClass(response.data.class.map(currentClass => <ClassComponent classObject={currentClass} />));
        setGrade(response.data.grade);
        setStudent(response.data.student);
        // classArray = ;
        // console.log(response);
        // fetch("http://127.0.0.1:8000/dashboard/")
        //     .then(res => res.json())
        //     .then(res => {
        //         console.log(res);
        //     })
        //     .catch(console.error);
    }, [])
    return (
        <div>
            {classForUser}
        </div>
    )
}