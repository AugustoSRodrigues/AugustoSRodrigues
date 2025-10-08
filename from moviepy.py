from moviepy import VideoFileClip

def mp4_para_gif(input_mp4, output_gif, fps=10):
    clip = VideoFileClip(input_mp4)
    clip.duration = min(clip.duration, 5)  # Limita a duração a 10 segundos
    clip.write_gif(output_gif, fps=fps)
    print(f"GIF salvo em: {output_gif}")

if __name__ == "__main__":
    entrada = input("Digite o caminho do arquivo MP4: ")
    saida = input("Digite o caminho para salvar o GIF: ")
    mp4_para_gif(entrada, saida)