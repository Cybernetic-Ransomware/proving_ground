from pytube import YouTube


def to_download(link: str, target_resolution: str, alt_highest: bool = False) -> None:
    try:
        yt_object = YouTube(link)
        stream = yt_object.streams.get_by_resolution(target_resolution)
        stream.download()
    except AttributeError:
        to_download_optional(link, alt_highest)
    else:
        print('Successfull completed!')


def to_download_optional(link: str, switch_to_highest: bool) -> None:

    try:
        yt_object = YouTube(link)

        if switch_to_highest:
            stream = yt_object.streams.get_highest_resolution()
            print('No resolution found, downloaded at highest found quality')
        else:
            stream = yt_object.streams.get_lowest_resolution()
            print('No resolution found, downloaded at lowest found quality')

        stream.download()
    except AttributeError:
        print('No video, check link and available resolutions')


if __name__ == '__main__':
    inp_link = str(input('Source link to video: '))
    inp_resolution = str(input('Resolution: '))

    to_download(inp_link, inp_resolution)
