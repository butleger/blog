class BaseAjaxWorker(TemplateView):
    #request and response worker are callbacks that takes response_data
    #and do some operations with them in the start and in the end
    request_callback = None
    response_callback = None
    #names of this data_names is the keys for data that will be getted from request
    data_names = []
    from_request_data = {}
    response_class = HttpResponse
    #should be dictionary with keys from data_names and your own data
    to_response_data = {'test': 'test'}
    #names that should be getted from view (check next comment)
    view_args_names = []
    #arguements that you get when use <int:id> or something like this in the URL
    view_args = {}

    NO_DATA = 'None'

    def setup(self, request, *args, **kwargs):
        #get data that will be getted in view
        #and put it in the class data
        for name in self.data_names:
            self.view_args[name] = kwargs.get(name, self.NO_DATA)

        if request.method == 'POST':
            for name in self.data_names:
                self.from_request_data[name] = request.POST(name, self.NO_DATA)
        if request.method == 'GET':
            for name in self.data_names:
                self.from_request_data[name] = request.GET(name, self.NO_DATA)

        if self.request_callback is not None:
            self.request_callback(self.to_response_data)

        return super().setup(request, *args, **kwargs)
    #redefinition cause should not do more complicated logic with templates
    def get(self, request, *args, **kwargs):
        if self.response_callback is not None:
            self.response_callback(self.to_response_data)
        return self.response_class(self.to_response_data)

    #this method allows you use viewclasses with post methods
    def post(self):
        if self.response_callback is not None:
            self.response_callback(self.to_response_data)
        return self.response_class(self.to_response_data)


class BaseBlogView(TemplateView):
    #should define template_name in next classes
    template_name = 'navigate_menu\\articles.html'
    base_context = {
        'footer': getFooter(),
        'menu': getMenu(),
    }

    def get_context_data(self, **kwargs):
        if self.base_context is not None:
            self.extra_context.update(**self.base_context)
        return super().get_context_data(**kwargs)
