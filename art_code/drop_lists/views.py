from django.shortcuts import render
import requests


dict_term = {'s': 'service', 'b': 'brand', 'st': 'style'}

def get_data_api():
    headers = {
        'Cache-Control': 'no-cache, no-store, must-revalidate'
    }
    service = requests.get('https://onboarding.art-code.team/api/test/v1/search/terms', headers=headers).json()['data']
    brand = requests.get('https://onboarding.art-code.team/api/test/v1/search/brands_terms', headers=headers).json()['data']
    style = requests.get('https://onboarding.art-code.team/api/test/v1/search/styles', headers=headers).json()['data']
    return {'s': service, 'b': brand, 'st': style}


def index(request):
    data = get_data_api()
    return render(request, 'main.html', context={'services': data['s'], 'brands': data['b'], 'styles': data['st']})


def first_choice(request, choice: str):
    data = get_data_api()
    choice = choice.split("-")
    data[choice[0]] = [requests.get(f'https://onboarding.art-code.team/api/test/v1/search/parse_link?'
                               f'{dict_term[choice[0]]}_slug={"-".join(choice[1:])}').json()[dict_term[choice[0]]]]
    return render(request, 'main.html', context={'services': data['s'], 'brands': data['b'], 'styles': data['st']})


def second_choice(request, choice: str, choice_2: str):
    data = get_data_api()
    choice = choice.split("-")
    choice_2 = choice_2.split("-")
    data_api = requests.get(f'https://onboarding.art-code.team/api/test/v1/search/parse_link?'
                        f'{dict_term[choice[0]]}_slug={"-".join(choice[1:])}&'
                        f'{dict_term[choice_2[0]]}_slug={"-".join(choice_2[1:])}').json()
    data[choice[0]] = [data_api[dict_term[choice[0]]]]
    data[choice_2[0]] = [data_api[dict_term[choice_2[0]]]]
    return render(request, 'main.html', context={'services': data['s'], 'brands': data['b'], 'styles': data['st']})


def third_choice(request, choice: str, choice_2: str, choice_3: str):
    data = get_data_api()
    choice = choice.split("-")
    choice_2 = choice_2.split("-")
    choice_3 = choice_3.split("-")
    data_api = requests.get(f'https://onboarding.art-code.team/api/test/v1/search/parse_link?'
                            f'{dict_term[choice[0]]}_slug={"-".join(choice[1:])}&'
                            f'{dict_term[choice_2[0]]}_slug={"-".join(choice_2[1:])}&'
                            f'{dict_term[choice_3[0]]}_slug={"-".join(choice_3[1:])}').json()
    data[choice[0]] = [data_api[dict_term[choice[0]]]]
    data[choice_2[0]] = [data_api[dict_term[choice_2[0]]]]
    data[choice_3[0]] = [data_api[dict_term[choice_3[0]]]]
    return render(request, 'main.html', context={'services': data['s'], 'brands': data['b'], 'styles': data['st']})