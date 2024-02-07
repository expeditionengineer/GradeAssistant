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
    const [refresh, setRefresh] = React.useState(false);
    function onClickToggle() {
        setRefresh(!refresh);
    }

    useEffect( async () => {
        const response = await axios.get("http://127.0.0.1:8000/dashboard/", {
            headers: {
                Authorization: `Token ${props.token}`
            }
        });
        console.log(response.data);
        var studentArrayForClass = [];
        setClass(response.data.class.map(currentClass => {
            for (var i = 0; i < response.data.student.length; i++) {
                if (response.data.student[i].classRelation === currentClass.id) {
                    studentArrayForClass.push(response.data.student[i]);
                    studentArrayForClass[i].grade = [];
                    for (var j = 0; j < response.data.grade.length; j++) {
                        if (response.data.grade[j].students[0] === response.data.student[i].id) {
                            console.log(response.data.grade[j])
                            studentArrayForClass[i].grade.push(response.data.grade[j]);
                        }
                    }
                }
            }
            currentClass.student = studentArrayForClass;
            return <ClassComponent classObject={currentClass} token={props.token} />
        }));
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
    }, [refresh])
    return (
        <div>
            <button onClick={onClickToggle} id="refresh" >Refresh Classes</button>
            {classForUser}
        </div>
    )
}