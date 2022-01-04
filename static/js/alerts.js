// alerts
alertContainer = document.getElementById("alert__container");

const closeAlert = () => {
    alertContainer.classList.add("display__alert");
};
const alertTimeout = setTimeout(closeAlert, 2500);
