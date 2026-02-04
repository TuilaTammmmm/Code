
function changetab(sukien,tentab){
    sukien.preventDefault();
    document.querySelectorAll('.content').forEach(element => {
        element.classList.remove('active');
    });
    document.querySelectorAll('.menulink').forEach(element => {
        element.classList.remove('active');
    });
    document.getElementById(tentab).classList.add('active');
    sukien.target.classList.add('active');
}