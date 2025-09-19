from PIL import Image, ImageSequence
import os

def otimizar_gif(input_path, output_path, max_width=320, max_colors=64):
    # Abre o GIF
    with Image.open(input_path) as im:
        frames = []
        for frame in ImageSequence.Iterator(im):
            # Redimensiona mantendo proporção
            w, h = frame.size
            if w > max_width:
                ratio = max_width / float(w)
                new_size = (max_width, int(h * ratio))
                frame = frame.resize(new_size, Image.LANCZOS)
            # Reduz cores
            frame = frame.convert('P', palette=Image.ADAPTIVE, colors=max_colors)
            frames.append(frame)
        # Salva o novo GIF otimizado
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            optimize=True,
            duration=im.info.get('duration', 100),
            disposal=2
        )
    print(f'GIF otimizado salvo em: {output_path}')

if __name__ == '__main__':
    entrada = input('Digite o caminho do GIF de entrada: ')
    saida = input('Digite o caminho para salvar o GIF otimizado: ')
    otimizar_gif(entrada, saida)
