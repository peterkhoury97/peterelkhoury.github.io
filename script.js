document.documentElement.classList.add('js');

const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
toggle.hidden = false;
function closeMenu() {
  navigation.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && navigation.classList.contains('is-open')) {
    closeMenu();
    toggle.focus();
  }
});

const dialog = document.querySelector('#image-dialog');
const enlargedImage = document.querySelector('#enlarged-image');
let imageTrigger;
if (typeof dialog.showModal === 'function') {
  document.querySelectorAll('.screenshot-link').forEach((link) => {
    link.addEventListener('click', (event) => {
      // Preserve opening in another tab and the plain-image fallback.
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      imageTrigger = link;
      document.querySelector('#image-title').textContent = link.dataset.title;
      document.querySelector('#image-caption').textContent = link.dataset.caption;
      enlargedImage.src = link.href;
      enlargedImage.alt = link.querySelector('img')?.alt || link.dataset.title;
      dialog.showModal();
      document.body.classList.add('dialog-open');
    });
  });
  document.querySelector('#close-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.body.classList.remove('dialog-open');
    imageTrigger?.focus({ preventScroll: true });
  });
}
document.querySelector('#year').textContent = new Date().getFullYear();
