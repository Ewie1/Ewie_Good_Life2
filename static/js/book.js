const trainer = document.getElementById('book')

trainer.addEventListener('click', reservationModal)

function reservationModal() {
    let modal = document.getElementById('modal-1')
    modal.classList.add('show-modal')
}
