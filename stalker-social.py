import instaloader

def print_profile_info(profile):
    print(f'Username: {profile.username}')
    print(f'Nome Completo: {profile.full_name}')
    print(f'Biografia: {profile.biography}')
    print(f'Número de seguidores: {profile.followers}')
    print(f'Número de seguidos: {profile.followees}')
    print(f'Número de posts: {profile.mediacount}')
    print(f'É privado? {profile.is_private}')
    print(f'É verificado? {profile.is_verified}')

username = input('Digite o nome de usuário: ')

loader = instaloader.Instaloader()

try:

    profile = instaloader.Profile.from_username(loader.context, username)

    print_profile_info(profile)

    print("\nPosts mais recentes:")
    for post in profile.get_posts():
        print(f"Post: {post.url}")
        print(f"Legenda: {post.caption}")
        print(f"Likes: {post.likes}")
        print(f"Comentários: {post.comments}")
        print(f"Data de postagem: {post.date}")
        print()
except instaloader.exceptions.ProfileNotExistsException:
    print('O perfil não existe ou é privado.')