import httpx


class Client:
    SANDBOX_API_ROOT = "https://od-api-sandbox.oxforddictionaries.com/api/v2"
    PRODUCTION_API_ROOT = "https://od-api.oxforddictionaries.com/api/v2"

    def __init__(
        self,
        application_id,
        application_key,
        sandbox=False,
        default_language="en",
    ):
        assert application_id != "", (
            "application_id is empty. Please provide a valid application_id"
        )
        assert application_key != "", (
            "application_key is empty. Please provide a valid application_key"
        )

        self.application_id = application_id
        self.application_key = application_key
        self.api_root = self.SANDBOX_API_ROOT if sandbox else self.PRODUCTION_API_ROOT
        self.default_language = default_language
        self.headers = {"app_id": application_id, "app_key": application_key}
        self.client = httpx.AsyncClient()

    async def send_request(self, path, method="GET"):
        """Make a GET request to the API"""
        full_uri = self.api_root + "/" + path
        return await self.client.request(method, full_uri, headers=self.headers)

    # ENTRIES ENDPOINTS
    async def get_entries(self, word, language=None, fields=None, strict_match=True):
        """
        Retrieve dictionary information for a given word.

        Args:
            word (str): The word to look up
            language (str): Language code (e.g., 'en', 'en-gb')
            fields (list): Optional list of fields to include (definitions, pronunciations, examples, etymologies)
            strict_match (bool): Whether to use strict matching
        """
        try:
            language = language or self.default_language
            path = f"entries/{language}/{word.lower()}"
            params = {}
            if fields:
                params["fields"] = ",".join(fields)
            if not strict_match:
                params["strictMatch"] = "false"

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No entry information for {word} in {language}."

    async def get_info_about_word(self, word, language=None):
        """
        Get dictionary information for chosen word (legacy method).
        """
        return await self.get_entries(word, language or self.default_language)

    # LEMMAS ENDPOINT
    async def get_lemmas(
        self, word, language=None, lexical_category=None, grammatical_features=None
    ):
        """
        Retrieve the root form (lemma) of an inflected word.

        Args:
            word (str): The inflected word
            language (str): Language code
            lexical_category (str): Optional lexical category filter
            grammatical_features (dict): Optional grammatical features filter
        """
        try:
            language = language or self.default_language
            path = f"lemmas/{language}/{word.lower()}"
            params = {}
            if lexical_category:
                params["lexicalCategory"] = lexical_category
            if grammatical_features:
                for key, value in grammatical_features.items():
                    params[f"grammaticalFeatures.{key}"] = value

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No lemma found for {word} in {language}."

    # TRANSLATIONS ENDPOINT
    async def get_translations(
        self,
        word,
        source_language=None,
        target_language="es",
        fields=None,
        strict_match=True,
    ):
        """
        Retrieve translations for a given word between source and target languages.

        Args:
            word (str): The word to translate
            source_language (str): Source language code
            target_language (str): Target language code
            fields (list): Optional list of fields to include
            strict_match (bool): Whether to use strict matching
        """
        try:
            source_language = source_language or self.default_language
            path = f"translations/{source_language}/{target_language}/{word.lower()}"
            params = {}
            if fields:
                params["fields"] = ",".join(fields)
            if not strict_match:
                params["strictMatch"] = "false"

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No translation for {word} from {source_language} to {target_language}."

    async def translate(self, word, source_language=None, target_language="es"):
        """
        Get Translation for word from source language to target language (legacy method).
        """
        return await self.get_translations(
            word, source_language or self.default_language, target_language
        )

    # THESAURUS ENDPOINT
    async def get_thesaurus(self, word, language=None, fields=None, strict_match=True):
        """
        Retrieve synonyms and antonyms for a given word.

        Args:
            word (str): The word to look up
            language (str): Language code
            fields (list): Optional list of fields to include
            strict_match (bool): Whether to use strict matching
        """
        try:
            language = language or self.default_language
            path = f"thesaurus/{language}/{word.lower()}"
            params = {}
            if fields:
                params["fields"] = ",".join(fields)
            if not strict_match:
                params["strictMatch"] = "false"

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No thesaurus data for {word} in {language}."

    async def get_synonyms(self, word, language=None):
        """
        Get synonyms for chosen word (legacy method).
        """
        result = await self.get_thesaurus(word, language or self.default_language)
        if isinstance(result, dict):
            # Extract synonyms from thesaurus response
            return result
        return f"No synonyms for {word} in our current dictionaries."

    async def get_antonyms(self, word, language=None):
        """
        Get antonyms for chosen word (legacy method).
        """
        result = await self.get_thesaurus(word, language or self.default_language)
        if isinstance(result, dict):
            # Extract antonyms from thesaurus response
            return result
        return f"No antonyms for {word} in our current dictionaries."

    # SENTENCES ENDPOINT
    async def get_sentences(self, word, language=None, fields=None, strict_match=True):
        """
        Retrieve example sentences for a given word.

        Args:
            word (str): The word to get examples for
            language (str): Language code
            fields (list): Optional list of fields to include
            strict_match (bool): Whether to use strict matching
        """
        try:
            language = language or self.default_language
            path = f"sentences/{language}/{word.lower()}"
            params = {}
            if fields:
                params["fields"] = ",".join(fields)
            if not strict_match:
                params["strictMatch"] = "false"

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No sentence examples for {word} in {language}."

    async def use_in_sentence(self, word, language=None):
        """
        Examples of how to use word in sentence (legacy method).
        """
        return await self.get_sentences(word, language or self.default_language)

    # WORDS ENDPOINT
    async def get_words(
        self,
        language=None,
        query=None,
        fields=None,
        lexical_category=None,
        grammatical_features=None,
        limit=None,
        offset=None,
    ):
        """
        Retrieve definitions, pronunciations, word origins, and grammatical data.

        Args:
            language (str): Language code
            query (str): Search query
            fields (list): Optional list of fields to include
            lexical_category (str): Optional lexical category filter
            grammatical_features (dict): Optional grammatical features filter
            limit (int): Number of results to return
            offset (int): Offset for pagination
        """
        try:
            language = language or self.default_language
            path = f"words/{language}"
            params = {}
            if query:
                params["q"] = query
            if fields:
                params["fields"] = ",".join(fields)
            if lexical_category:
                params["lexicalCategory"] = lexical_category
            if grammatical_features:
                for key, value in grammatical_features.items():
                    params[f"grammaticalFeatures.{key}"] = value
            if limit:
                params["limit"] = str(limit)
            if offset:
                params["offset"] = str(offset)

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No words found for query in {language}."

    # INFLECTIONS ENDPOINT
    async def get_inflections(
        self,
        word,
        language=None,
        fields=None,
        lexical_category=None,
        grammatical_features=None,
        strict_match=True,
    ):
        """
        Retrieve all inflected forms for a given lemma.

        Args:
            word (str): The lemma/root word
            language (str): Language code
            fields (list): Optional list of fields to include
            lexical_category (str): Optional lexical category filter
            grammatical_features (dict): Optional grammatical features filter
            strict_match (bool): Whether to use strict matching
        """
        try:
            language = language or self.default_language
            path = f"inflections/{language}/{word.lower()}"
            params = {}
            if fields:
                params["fields"] = ",".join(fields)
            if lexical_category:
                params["lexicalCategory"] = lexical_category
            if grammatical_features:
                for key, value in grammatical_features.items():
                    params[f"grammaticalFeatures.{key}"] = value
            if not strict_match:
                params["strictMatch"] = "false"

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No inflections found for {word} in {language}."

    # SEARCH ENDPOINTS
    async def search(
        self,
        language=None,
        query=None,
        prefix=None,
        regions=None,
        registers=None,
        domains=None,
        lexical_category=None,
        grammatical_features=None,
        limit=None,
        offset=None,
    ):
        """
        Search for possible matches for a given string using headword matching and fuzzy matching.

        Args:
            language (str): Language code
            query (str): Search query string
            prefix (str): Prefix search
            regions (list): Regions to filter by
            registers (list): Registers to filter by
            domains (list): Domains to filter by
            lexical_category (str): Optional lexical category filter
            grammatical_features (dict): Optional grammatical features filter
            limit (int): Number of results to return
            offset (int): Offset for pagination
        """
        try:
            language = language or self.default_language
            path = f"search/{language}"
            params = {}
            if query:
                params["q"] = query
            if prefix:
                params["prefix"] = prefix
            if regions:
                params["regions"] = ",".join(regions)
            if registers:
                params["registers"] = ",".join(registers)
            if domains:
                params["domains"] = ",".join(domains)
            if lexical_category:
                params["lexicalCategory"] = lexical_category
            if grammatical_features:
                for key, value in grammatical_features.items():
                    params[f"grammaticalFeatures.{key}"] = value
            if limit:
                params["limit"] = str(limit)
            if offset:
                params["offset"] = str(offset)

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No search results found in {language}."

    async def search_translations(
        self,
        source_language=None,
        target_language="es",
        query=None,
        prefix=None,
        regions=None,
        registers=None,
        domains=None,
        limit=None,
        offset=None,
    ):
        """
        Search for possible translations for a given string between source and target languages.

        Args:
            source_language (str): Source language code
            target_language (str): Target language code
            query (str): Search query string
            prefix (str): Prefix search
            regions (list): Regions to filter by
            registers (list): Registers to filter by
            domains (list): Domains to filter by
            limit (int): Number of results to return
            offset (int): Offset for pagination
        """
        try:
            source_language = source_language or self.default_language
            path = f"search/translations/{source_language}/{target_language}"
            params = {}
            if query:
                params["q"] = query
            if prefix:
                params["prefix"] = prefix
            if regions:
                params["regions"] = ",".join(regions)
            if registers:
                params["registers"] = ",".join(registers)
            if domains:
                params["domains"] = ",".join(domains)
            if limit:
                params["limit"] = str(limit)
            if offset:
                params["offset"] = str(offset)

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No translation search results found from {source_language} to {target_language}."

    async def search_thesaurus(
        self,
        language=None,
        query=None,
        prefix=None,
        regions=None,
        registers=None,
        domains=None,
        lexical_category=None,
        grammatical_features=None,
        limit=None,
        offset=None,
    ):
        """
        Search for possible thesaurus matches for a given string.

        Args:
            language (str): Language code
            query (str): Search query string
            prefix (str): Prefix search
            regions (list): Regions to filter by
            registers (list): Registers to filter by
            domains (list): Domains to filter by
            lexical_category (str): Optional lexical category filter
            grammatical_features (dict): Optional grammatical features filter
            limit (int): Number of results to return
            offset (int): Offset for pagination
        """
        try:
            language = language or self.default_language
            path = f"search/thesaurus/{language}"
            params = {}
            if query:
                params["q"] = query
            if prefix:
                params["prefix"] = prefix
            if regions:
                params["regions"] = ",".join(regions)
            if registers:
                params["registers"] = ",".join(registers)
            if domains:
                params["domains"] = ",".join(domains)
            if lexical_category:
                params["lexicalCategory"] = lexical_category
            if grammatical_features:
                for key, value in grammatical_features.items():
                    params[f"grammaticalFeatures.{key}"] = value
            if limit:
                params["limit"] = str(limit)
            if offset:
                params["offset"] = str(offset)

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"No thesaurus search results found in {language}."

    # UTILITY ENDPOINTS
    async def get_languages(self, source_language=None, target_language=None):
        """
        Retrieve available languages for monolingual or bilingual data.

        Args:
            source_language (str): Optional source language filter
            target_language (str): Optional target language filter
        """
        try:
            path = "languages"
            params = {}
            if source_language:
                params["sourceLanguage"] = source_language
            if target_language:
                params["targetLanguage"] = target_language

            if params:
                path += "?" + "&".join([f"{k}={v}" for k, v in params.items()])

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return "Unable to retrieve available languages."

    async def get_lexical_categories(self, language=None):
        """
        Retrieve available lexical categories for a given language.

        Args:
            language (str): Language code
        """
        try:
            language = language or self.default_language
            path = f"lexicalCategories/{language}"
            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"Unable to retrieve lexical categories for {language}."

    async def get_grammatical_features(self, language=None):
        """
        Retrieve available grammatical features for a given language.

        Args:
            language (str): Language code
        """
        try:
            language = language or self.default_language
            path = f"grammaticalFeatures/{language}"
            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"Unable to retrieve grammatical features for {language}."

    async def get_registers(
        self, language=None, source_language=None, target_language=None
    ):
        """
        Retrieve available registers for a given language or language pair.

        Args:
            language (str): Language code for monolingual registers
            source_language (str): Source language for bilingual registers
            target_language (str): Target language for bilingual registers
        """
        try:
            language = language or self.default_language
            if source_language and target_language:
                path = f"registers/{source_language}/{target_language}"
            else:
                path = f"registers/{language}"

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"Unable to retrieve registers for the specified language(s) for {language}."

    async def get_domains(
        self, language=None, source_language=None, target_language=None
    ):
        """
        Retrieve available domains for a given language or language pair.

        Args:
            language (str): Language code for monolingual domains
            source_language (str): Source language for bilingual domains
            target_language (str): Target language for bilingual domains
        """
        try:
            language = language or self.default_language
            if source_language and target_language:
                path = f"domains/{source_language}/{target_language}"
            else:
                path = f"domains/{language}"

            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"Unable to retrieve domains for the specified language(s) for {language}."

    async def get_regions(self, language=None):
        """
        Retrieve available regions for a given language.

        Args:
            language (str): Language code
        """
        try:
            language = language or self.default_language
            path = f"regions/{language}"
            response = await self.send_request(path)
            return response.json() if response.status_code == 200 else response
        except Exception:
            return f"Unable to retrieve regions for {language}."
