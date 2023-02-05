const trainer = document.getElementById('book')

trainer.addEventListener('click', reservationModal)

function reservationModal() {
    let modal = document.getElementById('bookTrainer')
    modal.classList.add('show-modal')
}
