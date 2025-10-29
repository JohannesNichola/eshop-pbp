function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Hapus semua class lama
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800',
        'bg-purple-600', 'border-purple-400', 'text-white',
        'bg-pink-700', 'border-pink-400', 'text-white'
    );

    // Gaya berdasarkan tipe
    if (type === 'success') {
        // Ungu khas Offside
        toastComponent.classList.add(
            'bg-gradient-to-r', 'from-purple-600', 'to-fuchsia-600',
            'border-purple-400', 'text-white', 'shadow-[0_0_20px_rgba(168,85,247,0.5)]'
        );
        toastComponent.style.border = '1px solid #c084fc';
    } else if (type === 'error') {
        // Warna merah tapi tetap nyatu dengan tema ungu
        toastComponent.classList.add(
            'bg-gradient-to-r', 'from-pink-700', 'to-purple-800',
            'border-pink-400', 'text-white', 'shadow-[0_0_20px_rgba(236,72,153,0.5)]'
        );
        toastComponent.style.border = '1px solid #f472b6';
    } else {
        // Default normal
        toastComponent.classList.add(
            'bg-white/10', 'backdrop-blur-md', 'border-purple-400/30', 
            'text-purple-200', 'shadow-lg'
        );
        toastComponent.style.border = '1px solid rgba(192,132,252,0.3)';
    }

    // Isi konten
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Animasi muncul
    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Hilang otomatis
    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
